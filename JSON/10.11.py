import json


def check_favorite_number():
	"""Получает уже записаное число пользователя."""
	filename = 'favorite_number.json'
	try:
		with open(filename) as f:
			fav_number = json.load(f)
	except FileNotFoundError:
		return None
	else:
		return fav_number


def get_favorite_number():
	"""Запрашивает новое число пользователя."""
	fav_number = input("What is your favorite number? ")
	filename = 'favorite_number.json'
	with open(filename, 'w') as f:
		json.dump(fav_number, f)
	return fav_number


def tell_fav_number():
	"""Отвечает пользователю о том, что уже знает любимое число."""
	fav_number = check_favorite_number()
	if fav_number:
		print(f"I know your favorite number, It's {fav_number}!")
	else:
		fav_number = get_favorite_number()
		print(f"OK, I will try remember your favorite number!")


tell_fav_number()
