def make_pizza(size, *toppings):
	"""Gives pizza's info"""
	print(f"Making a {size}-inch pizza with the following toppings:")
	for topping in toppings:
		print(f" - {topping}")