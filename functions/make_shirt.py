def make_shirt(size, text):
	print(f"Size of shirt is {str(size)}. Text is {text.upper()}.")

make_shirt(12, 'HERO')

def make_shirt2(size, text='FOTH'):
	print(f"Size of shirt is {str(size)}. Text is {text.upper()}.")

make_shirt2(44)

def make_shirt3(size='L', text='I love Python'):
	print(f"Size of shirt is {str(size)}. Text is {text.upper()}.")

make_shirt3()
make_shirt3(45, 'WHERE is my mind?')

def describe_city(city, country='Belarus'):
	print(f"The {city.title()} is in {country.title()}!")

describe_city('gomel')
describe_city('minsk')
describe_city('los angeles', 'usa')
