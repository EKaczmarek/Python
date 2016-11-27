print('Kalkulator objetosci')
a = float(input('a: '))
b = float(input('b: '))
h = float(input('Wysokosc: ' ))
obj = a * b * h
print('Objetosc wynosi: ' + str(obj))

if a == b:
	print('Bryla ma podstawe kwadratu')
elif a == b == h:
	print('Bryla jest szescianem')
else:
	print('Bryla jest prostopadloscianem')
	
raw_input()