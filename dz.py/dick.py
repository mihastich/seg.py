#name = 'Иван'
#age = 35
#car = True
friends = {
    'name': 'Иван',
    'age' : 35,
    'car' : True
}
print(friends)
print(len(friends))
print(type(friends))

friends['wife'] = False              # добавить
print(friends)

friends['wife'] = True              # изменить
print(friends)

del friends['wife']                 # удалить
print(friends)

print(friends.keys())               # получить ключи
print(friends.values())             # получить значения

print(friends.items())
print(list(friends.items()))
print('Иван' in friends.values())







