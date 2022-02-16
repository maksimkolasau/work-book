filename = 'programming.txt'

with open('programming.txt', 'w') as file_object:
	file_object.write("I love programming.\n")

with open('programming.txt', 'a') as file_object2:
	file_object2.write('I also love finding meaning in large datasets.\n')
	file_object2.write('I love creating apps that can run in a browser.\n')


# r+ - РЕЖИМ ЧТЕНИЯ И ЗАПИСИ
# r - РЕЖИМ ЧТЕНИЯ
# a - РЕЖИМ ПРИСОЕДИНЕНИЯ
# w - РЕЖИМ ЗАПИСИ
