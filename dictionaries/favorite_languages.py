favorite_languages = {
	'jen': 'pyhton',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python'
}

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for k, v in favorite_languages.items():
	print(f"\nName: {k.title()}")
	print(f"Language: {v.title()}")

print("\n")

for name, language1 in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language1.title()}.")

for name1 in favorite_languages.keys():
	print(name1.title())

print('\n')
# dlya konkretnih ludey iz spiska soobshenie
friends = ['phil', 'sarah']
for name2 in favorite_languages.keys():
	if name2 in friends:
		language2 = favorite_languages[name2].title()
		print(f"\t{name2.title()}, I see you love {language2}!")

print('\n')
# proveryaem est li chelovek v spiske i esli net to vyvodim soobshenie
if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

# sortiryem slovar
for name3 in sorted(favorite_languages.keys()):
	print(f"{name3.title()}, thank you for taking the poll!")

