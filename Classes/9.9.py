class Car():

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0


	def get_descriptive_name(self):
		long_name = f"{self.make.title()} {self.model.title()} {self.year}"
		return long_name


	def read_odometer(self):
		print(f"This car has {self.odometer_reading} miles on it.")


	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")


	def increment_odometer(self, miles):
		self.odometer_reading += miles


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


	def upgrade_battery(self):
		if self.battery_size != 100:
			self.battery_size = 100


elcar1 = ElectricCar('tesla', 'model s', 2019)
elcar1.battery.get_range()
elcar1.battery.upgrade_battery()
elcar1.battery.get_range()