class Restaurant():
#                      АТРИБУТЫ: параметры для каждого экземпляра
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

#     МЕТОДЫ: что делает тот или иной экземпляр

	def describe(self):
		print(f"The {self.restaurant_name} restaurant has the {self.cuisine_type} cuisine!")


	def open_restaurant(self):
		print(f"The {self.restaurant_name} restaurant is open now!")

