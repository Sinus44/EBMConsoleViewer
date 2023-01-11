import datetime

class Logging:
	"""Запись отладочной информации в файл"""

	def log(*text):
		"""Логирование в файл"""
		date = datetime.datetime.now()
		file = open(f"{date.day}{date.month}{date.year}.log", "a")

		for i in text:
			i = str(i)
			file.write(f"[{'{:2.0f}'.format(date.hour)}:{'{:2.0f}'.format(date.minute)}:{'{:2.0f}'.format(date.second)}]: {str(i)}\n")

		file.close()