cats = 'cats.txt'
dogs = 'dogs.txt'
try:
	with open(cats) as c:
		cats_open = c.read()
		print(cats_open)
	with open(dogs) as d:
		dogs_open = d.read()
		print(dogs_open)
except FileNotFoundError:
	pass

