def get_formatted_city_country(city, country, population=''):
	"""Строит отформатированное полное имя."""
	if population:
		full_name = f"{city}, {country} - {population}."
	else:
		full_name = f"{city}, {country}."
	return full_name.title()