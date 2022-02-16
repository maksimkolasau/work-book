import restaurant

restaurant = restaurant.Restaurant('Golden', 'chinese')

print(f"I'm going to {restaurant.restaurant_name} restaurant tonight!")
print(f"I love {restaurant.cuisine_type} cuisine!")

restaurant.describe()
restaurant.open_restaurant()