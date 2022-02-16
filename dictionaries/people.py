ksusha = {
	'first_name': 'kseniya',
	'last_name': 'komandyshko',
	'age': 28,
	'city': 'minsk'
}

ivan = {
	'first_name': 'ivan',
	'last_name': 'ivanov',
	'age': 29,
	'city': 'moscow'
}

maks = {
	'first_name': 'maks',
	'last_name': 'kolasau',
	'age': 31,
	'city': 'minsk'
}

people = [ksusha, ivan, maks]

for person in people:
	print(f"\nFull Name: {person['first_name'].title()} {person['last_name'].title()}")
	print(f"\tAge: {person['age']}")
	print(f"\tCity: {person['city'].title()}")