import unittest
from city_functions import get_formatted_city_country

class CCTestCase(unittest.TestCase):
	"""Тесты для 'city_functions.py'"""
	def test_city_country(self):
		"""Названия вида 'Santiago, Chile' работают правильно?"""
		formatted_name = get_formatted_city_country('minsk', 'belarus')
		self.assertEqual(formatted_name, 'Minsk, Belarus.')


	def test_city_country_population(self):
		"""Названия с популяцией работаю верно?"""
		formatted_name = get_formatted_city_country('minsk', 'belarus', 'population=9000000')
		self.assertEqual(formatted_name, 'Minsk, Belarus - Population=9000000.')

if __name__ == '__main__':
	unittest.main()