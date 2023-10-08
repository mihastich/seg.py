car = 'toiota camri gracia'
car_length = len(car)
print(car_length)

car_upper = car.upper()
print(car_upper)

car = 'toiota camri gracia'
ad = 'rac'
#print('rac' in car)
print(ad in car)
if ad in car:
    print('есть')

new_car = car.replace('gracia', 'grant')
print(new_car)
#help(ctr)
#print(dir(str))
print(car.upper())
print(car.lower())
print(car.title())
print(car.isdigit())
print(car.split())
car = 'toiota;;;camri;;;gracia'
print(car.split(';;;'))

name = 'toiota'
model = 'camri'
info = 'марка: {},  модель: {}'.format(name,model)
print(info)

info = f'марка: {name},  модель: {model}'
print(info)









