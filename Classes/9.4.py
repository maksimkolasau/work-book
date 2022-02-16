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


	def read_served(self):
		print(f"{self.restaurant_name} served {self.number_served} numbers.")


	def increment_served(self, served_nums):
		self.number_served += served_nums


restaurant = Restaurant('Golden', 'chinese')
restaurant.read_served()
restaurant.increment_served(23)
restaurant.read_served()
restaurant.increment_served(55)
restaurant.read_served()