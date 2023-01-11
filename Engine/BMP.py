from Engine.Byte import Byte

class BMP:
	"""Импорт файлов *.bmp, получение данных из файла и их структуризация"""
	
	def __init__(self, path):
		"""Импорт файлов *.bmp, получение данных из файла и их структуризация"""
		self.path = path

		self.file = open(path, "rb")
		self.dataBytes = self.file.read()
		self.file.close()
		self.dataHex = Byte.bytesToHex(self.dataBytes)

		if Byte.getHexBytesNormal(self.dataHex, 0, 1) != "424d":
			raise Exception("File type is not BMP")

		self.length = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("2"), Byte.hexToDec("5")))
		self.pixelDataOffset = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("a"), Byte.hexToDec("d")))
		self.bmpVersion = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("0e"), Byte.hexToDec("11")))

		if self.bmpVersion == 12: self.versionCode = "CORE"
		elif self.bmpVersion == 40: self.versionCode = "3"
		elif version == 108: self.versionCode = "4"
		elif version == 124: self.versionCode = "5"
		else: raise Exception("Unkown BMP version")

		if self.versionCode != "3":
			raise Exception("Unsupported BMP version")

		self.w = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("12"), Byte.hexToDec("15")))
		self.h = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("16"), Byte.hexToDec("19")))
		
		self.yDirection = self.h > 0
		self.h = abs(self.h)

		self.byteOnPixel = int(Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("1c"), Byte.hexToDec("1d"))) / 8)

		self.pixelStorageType = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("1e"), Byte.hexToDec("21")))
		if self.pixelStorageType != 0:
			raise Exception("Unsupported pixel storage type")

		self.pixelDataSize = Byte.hexToDec(Byte.getHexBytesReverse(self.dataHex, Byte.hexToDec("22"), Byte.hexToDec("25")))
		self.pixelData = self.dataHex[self.pixelDataOffset*2:]
		pixelData = self.pixelData + ""

		self.stringLen = 2 * self.byteOnPixel * self.w
		self.adding = int(self.stringLen / 2) % 4

		if self.adding != 0:
			self.adding = 4 - self.adding
		
		self.adding *= 2

		st = ""
		for i in range(self.h):
			st += pixelData[:self.stringLen]
			pixelData = pixelData[self.stringLen+self.adding:]

		pixels = []

		for i in range(self.h):
			pixels.append([])
			for j in range(self.w):
				slic = st[:6]
				st = st[6:]
				pixels[i].append(slic)

		buffer = []
		for i in range(self.h):
			arr = []
			for j in range(self.w):
				x1 = Byte.hexToDec(pixels[i][j][:2])
				x2 = Byte.hexToDec(pixels[i][j][2:4])
				x3 = Byte.hexToDec(pixels[i][j][4:])

				arr.append((x3, x2, x1))
			buffer.append(tuple(arr))

		self.buffer = tuple(buffer[::-1 if self.yDirection else 1])