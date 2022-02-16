cities = {
	'minsk': {
		'country': 'country: belarus',
		'population': 'population: 2 million people',
		'language': 'language: belorussian'
	},
	'piter': {
		'country': 'country: russia',
		'population': 'population: 4.9 million people',
		'language': 'language: russian'
	},
	'los angeles': {
		'country': 'country: united states of america',
		'population': 'population: 3.99 million people',
		'language': 'language: english'
	},
}

cities['milan'] = {
		'country': 'country: italy',
		'population': 'population: 1.35 million people',
		'language': 'language: italian',
}

for name in cities.keys():
	print(f"\nName of the city:\n\t{name.title()}")
	print(f"\nCity's info: ")
	for info in cities[name].values():
		print(f"\t{info.title()}")
