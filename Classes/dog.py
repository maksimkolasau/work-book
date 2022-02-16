class Dog():
	"""Simple model of a dog"""

	def __init__(self, name, age):
		"""Инициализирует атрибуты name и age."""
		self.name = name
		self.age = age

	def sit(self):
		"""Sobaka saditsya po komande"""
		print(f"{self.name} is now sitting.")

	def roll_over(self):
		"""Sobaka perekatyvaetsya po komande."""
		print(f"{self.name} is rolled over!")

my_dog = Dog('Grunya', 11)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
print('\n')
print(f"Your dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.roll_over()



