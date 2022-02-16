rivers = {
	'nile': 'egypt',
	'volga': 'russia',
	'svisloch': 'belarus',
}

for river, country in rivers.items():
	if river == 'svisloch':
		print(f"The {river.title()} runs through Minsk.")
	else:
		print(f"The {river.title()} runs through {country.title()}.")

for river2 in sorted(rivers.keys()):
	print(f"\n{river2.title()}")

for country2 in sorted(rivers.values()):
	print(f"\n{country2.title()}")