grunya = {
	'animal': 'bird',
	'owner': 'uri',
}

jackie = {
	'animal': 'dog',
	'owner': 'ksusha',
}

batty = {
	'animal': 'cat',
	'owner': 'maksim',
}

pets = [grunya, jackie, batty]

for pet in pets:
	print(f"\n{pet['owner'].title()} is the owner of the {pet['animal']}.")

