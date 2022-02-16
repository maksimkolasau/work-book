pizzas = ['Cheese', 'Barbeque', 'Lisitsa']

for pizza in pizzas:
	print("I like " + pizza + " pizza")
	print("I really love pizza!\n")

animals = ['dog', 'cat', 'cow']

for animal in animals:
	print("A " + animal.title() + " gives a milk to its babies!")
print("Any of these animals would make a great pet!\n")


friend_pizzas = pizzas[:]
pizzas.append('Mashroom')
friend_pizzas.append('Potato')

print(f"My favorite pizzas are: {pizzas}\n")
print(f"My friend's favorite pizzas are: {friend_pizzas}\n")