import wave
import pyaudio
import threading

class Sound:
	"""Импортирование звуков из файла, воспроизведение"""

	def __init__(self, filePath):
		"""Импортирование звуков из файла, воспроизведение"""
		self.filePath = filePath
		self.chunksize = 1024
		self.volume = 1
		self.off = False
		
		self.portaudio = pyaudio.PyAudio()
		self.thread = threading.Thread(target=self.p)  

		wavefile = wave.open(self.filePath, 'r')

		self.format = self.portaudio.get_format_from_width(wavefile.getsampwidth())
		self.channels = wavefile.getnchannels()
		self.defaultRate = wavefile.getframerate()
		self.rate = self.defaultRate

	def p(self):
		"""Функция потока воспроизведения"""
		wavefile = wave.open(self.filePath, 'r')

		self.streamobject = self.portaudio.open(format=self.format, channels=self.channels, rate=self.rate, output=True ) 
		self.data = wavefile.readframes(self.chunksize)

		while len(self.data) > 0 and not self.off:
			if self.off: return
			self.streamobject.write(self.data)
			self.data = wavefile.readframes(self.chunksize)

	def speed(self,speed):
		"""Установка скорости воспроизведения"""
		self.speed(speed)
		self.rate = int(self.defaultRate * speed)

	def play(self):
		"""Запуск потока воспроизведения"""
		self.off = False
		if not self.thread.is_alive():
			self.thread = threading.Thread(target=self.p)
			self.thread.start()

	def volume(volume):
		"""Установка громкости"""
		self.volume = volume

	def stop(self):
		"""Остановка воспроизведения"""
		self.off = True
