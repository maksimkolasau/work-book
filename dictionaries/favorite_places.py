favorite_places = {
	'luba': {
		'place_1': 'egypt',
		'place_2': 'triund mountain',
	},
	'maks': {
		'place_1': 'goa',
		'place_2': 'triund mountain',
		'place_3': 'eifel tower'
	}
}

for name in favorite_places.keys():
	print(f"Name: \n\t{name.title()}")
	print(f"Favorite places: ")
	for n in favorite_places[name].values():
		print(f"\t{n.title()}")


