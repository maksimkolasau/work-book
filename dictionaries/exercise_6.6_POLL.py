favorite_languages = {
	'petya': 'c++',
	'vasya': 'python',
	'ivan': 'java',
	'igor': 'javascript',
	'maks': 'python',
}

poll_list = ['luba', 'ivan', 'kostya', 'vasya', 'zhenya', 'ksusha', 'petya', 'igor', 'maks', 'boris']
print(len(poll_list))

for name in poll_list:
	if name in favorite_languages.keys():
		print(f"Thank you, {name.title()}, for completing our survey!")
	else:
		print(f"{name.title()}, please take a participation in the POLL!")
