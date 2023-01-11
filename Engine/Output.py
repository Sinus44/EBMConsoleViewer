import ctypes
import os

class Output:
	"""Настройка выходного буффера окна консоли"""

	def init(mode=5):
		"""Иницаилизация окна консоли"""
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.SetConsoleMode(handle, mode)
	
	def getTitle():
		"""Получение заголовка окна консоли"""
		out = (ctypes.c_char * 128)()
		ctypes.windll.kernel32.GetConsoleTitleW(ctypes.byref(out), ctypes.wintypes.DWORD(256))
		return str(bytes(out), encoding="utf-8")

	def title(title="Console Engine by Sinus"):
		"""Установка заголовка окна консоли"""
		ctypes.windll.kernel32.SetConsoleTitleW(title)
	
	def resize(w=60, h=40):
		"""Установка размера буффера окна консоли (в символах)"""
		os.system(f'mode con cols={w} lines={h}')
