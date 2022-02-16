navy_book = 'Our_Navy_at_war.txt'

with open(navy_book) as book:
	word_the = book.read()
	c = word_the.count('than')
	print(c)
