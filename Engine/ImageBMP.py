from Engine.Color import Color
from Engine.BMP import BMP

class ImageBMP(BMP):
	"""Импорт картинок пригодных для вставки в Window, из формата *.bmp"""
	
	def __init__(self, path, alpha=False):
		"""Импорт картинок пригодных для вставки в Window, из формата *.bmp"""
		super().__init__(path)
		self.alpha = alpha
		self.alphaColor = (0, 0, 0)
		self.contentBuffer = self.buffer
		
		self.buffer = []
		for y in range(self.h):
			self.buffer.append([])
			for x in range(self.w):
				color = self.contentBuffer[y][x]
				self.buffer[y].append(self.getColor(color))

	def getColor(self, color):
		"""Внутренний метод для преобразования кортежа цвета в символ-код"""
		if self.alphaColor == color:
			return 0

		return Color.Background.rgb(color[0], color[1], color[2]) + " "