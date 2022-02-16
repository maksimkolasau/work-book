fav_nums = {
	'ksusha': {
		'number1': 76,
		'number2': 24,
		'number3': 123
	},
	'luba': {
		'number1': 24,
		'number2': 123
	},
}

for name in fav_nums.keys():
	print(f"Name:\n\t{name.title()}")
	print(f"Favorite numbers: ")
	for numbers in fav_nums[name].values():
		print(f"\t{numbers}")
