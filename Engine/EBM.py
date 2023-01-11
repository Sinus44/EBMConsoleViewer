from Engine.Byte import Byte

class EBM:
	"""Импорт файлов *.ebm, получение данных из файла и их структуризация"""
	
	def __init__(self, path):
		"""Импорт файлов *.ebm, получение данных из файла и их структуризация
		EBM(str path) - path-путь к файлу для чтения
		EBM(list path OR tuple path) - дву мерный массив кортежей цветов пикселей для конвертации в файл
		"""

		if type(path) == type(""):
			self.path = path
			self.readFromFile()

		elif type(path) in [type(tuple([])), type([])]:
			self.convertArrayToEBM(path)

	def convertArrayToEBM(self, array):
		w = len(array[0])
		h = len(array)

		pixelsHex = ""
		for string in array:
			for pixel in string:
				for component in pixel:
					#print(Byte.hexToFixedHex(Byte.decToHex(component), 2))
					pixelsHex += Byte.hexToFixedHex(Byte.decToHex(component), 2)

		outBytes = f"""{Byte.bytesToHex(Byte.stringToBytes("EBM"))}{Byte.hexToFixedHex(Byte.decToHex(w), 4)}{Byte.hexToFixedHex(Byte.decToHex(h), 4)}{pixelsHex}"""
		self.readFromHex(outBytes)

	def readFromFile(self):
		self.dataBytes = b""
		self.dataHex = ""
		self.pixelsCount = -1


		file = open(self.path, "rb")
		self.dataBytes = file.read()
		self.dataHex = Byte.bytesToHex(self.dataBytes)
		file.close()
		self.readFromHex(self.dataHex)

	def readFromHex(self, hex):
		self.dataHex = hex

		if Byte.getHexBytesSize(self.dataHex, Byte.hexToDec("0"), 3) != "45424d":
			raise Exception("Incorrect type")

		self.w = Byte.hexToDec(Byte.getHexBytesSize(self.dataHex, Byte.hexToDec("3"), 2))
		self.h = Byte.hexToDec(Byte.getHexBytesSize(self.dataHex, Byte.hexToDec("5"), 2))
		self.pixelsCount = self.w * self.h

		pixelsHexData = self.dataHex[Byte.hexToDec("7")*2:]
		pixelsHexArray = []

		for _ in range(self.pixelsCount):
			pixelData = pixelsHexData[:6]
			pixelsHexData = pixelsHexData[6:]
			pixelsHexArray.append(pixelData)

		array = []
		for i in range(self.h):
			string = []
			for j in range(self.w):
				pos = i * self.w + j

				x1 = Byte.hexToDec(pixelsHexArray[pos][:2])
				x2 = Byte.hexToDec(pixelsHexArray[pos][2:4])
				x3 = Byte.hexToDec(pixelsHexArray[pos][4:])

				string.append((x1, x2, x3))

			array.append(tuple(string))

		self.buffer = tuple(array)

	def saveToFile(self, fileName):
		file = open(fileName, "wb")
		#print(Byte.hexStringToBytes(self.dataHex))
		file.write(Byte.hexStringToBytes(self.dataHex))
		file.close()