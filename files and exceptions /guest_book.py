name = "\nPlease enter a name: "
guests_book = 'guests_book.txt'

with open(guests_book, 'a') as gs:
	while True:
		names = input(name)

		if names == 'stop':
			break
		else:
			print(f"Hello, {names.title()}!")
			gs.write(f"Hello, {names.title()}!\n")()



