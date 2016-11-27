
print('Lista zakupow od Eli')

lista = []
x = 0
while  x != 5:
	b = input('Co masz kupic? '),
	lista.append(b)
	x += 1
	
print(str(lista))

print('\n A Rafal jak zwykle swoje :)')

y = 0
lista1 = []
while y != 5:
	a = input('Co kupiles?: '),
	lista1.append(str(a)),
	y += 1
	

l = set(lista)
l1 = set(lista1)

print ('Rafale kupiles: ' + str(l.intersection(l1)))
print ('Rafale nie kupiles: ' + str(l.difference(l1)))


