import ctypes
import sys

class Admin:
	"""Запуск от имени адмнистратора"""

	def checkAdmin():
		"""Возвращает True если скрипт запущен от имени администратора"""
		return bool(ctypes.windll.shell32.IsUserAnAdmin())

	def restartAsAdmin():
		"""Перезапускает скрипт с правами администратора"""
		ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable,__file__, None, 1)
		exit()