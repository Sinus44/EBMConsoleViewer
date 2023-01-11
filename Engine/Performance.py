import time
import timeit

class Performance:
	"""Замер времени выполнения кода"""
	
	startTime = 0
	
	def start():
		"""Указывает начальное время отсчета"""
		Performance.startTime = time.time()
	
	def time():
		"""Возвращает время прошедшее с точки отсчета"""
		return time.time() - Performance.startTime

	def function(f, repeats=1, count=1):
		"""Возвращает время выполнения функции"""
		return timeit.repeat(f, repeat=repeats, number=count)