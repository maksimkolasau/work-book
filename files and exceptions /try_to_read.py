file_path = '/home/kolasau_/Downloads/Эрик_Мэтиз_Изучаем_Python_Библиотека_2020.pdf'

with open(file_path) as book:
	lines = book.readlines()

print(len(lines))
