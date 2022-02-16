from car import Car

class ElectricCar(Car):
	"""представляет аспекты машины, специфические для электромобилей"""

	def __init__(self, make, model, year):
		"""инициализирует атрибуты класса-родителя
		затем инициализирует атрибуты, специфические для электромобиля."""
		super().__init__(make, model, year)
		self.battery = Battery()


class Battery():

	def __init__(self, battery_size=75):
		self.battery_size = battery_size

	def describe_battery(self):
		"""выводит информацию о мощности аккумулятора."""
		print(f"This car has a {self.battery_size}-kWh battery.")

	def get_range(self):
		"""выводит приблизительный запас хода аккумулятора."""
		if self.battery_size == 75:
			range = 260
		elif self.battery_size == 100:
			range = 315
		print(f"This car can go about {range} miles on a full charge.")