mai_list_a = list(input('Введите несколько чисел через заятую : '))
mai_list_b = list(input('Введите несколько чисел через заятую : '))
print(type(mai_list_a))
print(type(mai_list_b))
print(mai_list_a)
print(mai_list_b)
#mai_list = ((mai_list_a) + (mai_list_b))
#print(mai_list)
#print(set(mai_list))
mai_list_a.extend(mai_list_b)
print(mai_list_a)
print(set(mai_list_a))