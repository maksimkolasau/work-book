banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
	print(f"{user.title()}, you can post a response if you wish.")

# 1___________________________________________________

x = ('1', '2', 123123, '098')
y = 2

if y in x:
	print('True')
else:
	print('False')

# 2___________________________________________________

car = 'subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'Audi')

# 3___________________________________________________

pictures = ['mikola', 'ivan']
pic = 'mikola'

if pic in pictures:
	print(pic.title())

# 4___________________________________________________

soup_menu = ['borsh', 'shee', 'soup s frikadelkami']

if 'molochniy soup' not in soup_menu:
	soup_menu.append('molochniy soup')
	print('Now we have molochniy soup')
	print(soup_menu[3].title())

# 5___________________________________________________

grand = ['cafe', 'royal', 'kitchen']

for g in grand:

	if g == 'cafe':
		print('CAFE')
	if g == 'royal':
		print(g.upper())
	else:
		print('False')

# 6___________________________________________________

print(10 != 5)

# 7___________________________________________________

z = 123
v = 321

print(z == v)

# 8___________________________________________________


characters = ['paul', 'misha']

if 'max' not in characters:
	characters.append('max')
	print(characters[2].title())
	print(characters)
