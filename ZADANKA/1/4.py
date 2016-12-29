def czy_pierwsza(n):
	counter = 0;
	for i in range(1,n):
		if(n % int(i) == 0):
			counter += 1
	if(counter >= 2 or n == 1):
		return False
	elif(counter < 2):
		return True
		
def naSlownik(lista):
	Slownik = {}
	for i in lista:
		Slownik[i] = lista.count(i)
	for i in Slownik:
	  print("(" + str(i) + ", " + str(Slownik[i]) + ")")

def rozklad(n):
	lista = []
	for i in range(2,n-1):
			while(n % int(i) == 0 and czy_pierwsza(int(i)) == True):
				lista.append(i)
				n = n / int(i)
	naSlownik(lista)

rozklad(19999)
