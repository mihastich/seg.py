fruts = ['яблоко','апельсин','киви']
print(fruts)
fruts.append('сметана')
print(fruts)
frutsnon = ['арбуз','малина','киви','свекла']
fruts.extend(frutsnon)
print(fruts)
fruts.reverse()
print(fruts)
fruts.pop(3)
print(fruts)
fruts.remove('киви')
print(fruts)
print(len(fruts)) # количество элементов списка
print('стакан' in fruts)



