class Byte:
	"""Работа с данными BYTES-HEX-DEC-STRING"""

	def stringToBytes(string):
		return bytes(string, "utf-8")

	def hexToFixedHex(hex, length):
		"""Добавляет нули до определенного кол-ва длины всей строки"""
		return ("0" * (length - len(hex))) + hex

	def bytesToInt(b):
		"""Преобразует BYTES в INT"""
		return int(b)

	def bytesToHex(b):
		"""Преобразует BYTES в HEX"""
		return b.hex()

	def hexStringToBytes(hex):
		"""Преобразует HEX_STRING в BYTES"""
		outBytes = b""
		for i in range(0, len(hex),2):
			outBytes += Byte.hexToBytes(hex[i:i+2])

		return outBytes
	
	def hexToBytes(hex):
		"""Преобразует HEX в BYTES"""
		return Byte.decToBytes(Byte.hexToDec(hex))
	
	def hexToDec(hex):
		"""Преобразует HEX в INT"""
		return int(hex, base=16)

	def decToHex(dec):
		"""Преобразует INT в HEX"""
		return hex(dec)[2:]
	
	def decToBytes(dec):
		"""Преобразует INT в BYTES"""
		return dec.to_bytes(1, 'little')

	def getHexByte(hex, pos):
		"""Возвращает HEX_BYTE из HEX_STRING по номеру позиции"""
		return hex[pos * 2] + hex[pos * 2 + 1]

	def getHexBytesSize(hex, pos, size):
		"""Возвращает HEX_BYTES из HEX_STRING с начальной позиции указанной длиной"""
		return Byte.getHexBytesNormal(hex, pos, pos + size - 1)

	def getHexBytesNormal(hex, startPos, endPos):
		"""Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной"""
		return hex[startPos*2:(endPos+1)*2]

	def getHexBytesReverse(hex, startPos, endPos):
		"""Возвращает HEX_BYTES из HEX_STRING по номеру позиции начальной и конечной, обратный порядок байт"""
		outStr = ""
		
		for i in range(endPos, startPos - 1, -1):
			outStr += Byte.getHexByte(hex, i)
	
		return outStr
