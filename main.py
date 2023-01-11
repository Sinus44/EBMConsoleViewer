from Engine import *
import sys

if __name__ == "__main__":
	print("=" * 90)

	if  not len(sys.argv) > 1:
		filename = input("Введите название файла для просмотра: ")
	else:
		filename = sys.argv[1].split("\\")[-1].split(".")[0]

	img = ImageEBM(filename+".ebm")

	Output.resize(img.w, img.h + 1)
	screen = Window(img.w, img.h)

	screen.fill()
	screen.paste(img)
	screen.draw()
	input(f"Файл {filename} успешно отображен. Нажмите Enter для выхода.")