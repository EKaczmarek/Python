
def czy_pierwsza(n):
	counter = 0;
	for i in range(1,n):
		if(n % int(i) == 0):
			counter += 1
	if(counter >= 2 or n == 1):
		return False
	elif(counter < 2):
		return True

def rozklad(n):
	lista = []
	for i in range(1,n-1):
		if(n % int(i) == 0 and czy_pierwsza(int(i)) == True):
			if(czy_pierwsza(int(i)) == True):
				lista.append(i)
			print(lista)


rozklad(712)
