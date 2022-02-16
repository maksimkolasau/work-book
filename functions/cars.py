
def make_car(car_name, model_name, **car_info):
	car_info['car_name'] = car_name
	car_info['model_name'] = model_name
	return car_info



car = make_car('subaru', 'outback', color='black', tow_package=True)
print(car)