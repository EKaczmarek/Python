
from random import randint

def rzut_kostka():
	return randint(1,6)

def wyj_imie():
	try:
		imie = str(input('Podaj imie gracza'))
		if imie.isnumeric() == True:
			raise ValueError('')
		else:
			return imie
	except ValueError:
		tak_nie()

def tak_nie():
	try:
		output = str(input('Czy chcesz grac jeszcze raz T/N?')) 
		if output.isnumeric() == True:
			raise ValueError('')
		if(output == "T" or output == "N"):
			return str(output)
		else:
			raise ValueError('')
	except ValueError:
		tak_nie()

def bilans(_wygrana, tab1, tab2):
  
	if(int(tab1[0] + tab1[1]) > int(tab2[0]+tab2[1])):
		_wygrana.append('first')
	elif(int(tab1[0] + tab1[1]) < int(tab2[0]+tab2[1])):
		_wygrana.append('second')
	elif(int(tab1[0] + tab1[1]) == int(tab2[0]+tab2[1])):
		_wygrana.append('both')
	return _wygrana

def wynik(_wygrana):
	if(int(_wygrana.count('first')) > int(_wygrana.count('second'))):
		return 'first'
	elif(int(_wygrana.count('first')) < int(_wygrana.count('second'))):
		return 'second'
	elif(int(_wygrana.count('first')) ==  int(_wygrana.count('second'))):
		return 'both'
  
def przypisz(_tab, _Lista, _Slownik, _fise):
	_tab = []
	
	_tab.append(rzut_kostka())
	_tab.append(rzut_kostka())

	_Lista.append(_tab)
	_Slownik[_fise] = _Lista
		
	return _tab,_Lista, _Slownik

def main(): 
	Slownik = {}
	tab1, tab2 = [],[]
	wygrana,Lista1, Lista2 = [],[],[]
	los = -1

	#pierwszy gracz
	first = wyj_imie()
	#drugi gracz
	second = wyj_imie()

	while(True):
		los += 1
		tab1, Lista1, Slownik = przypisz(tab1, Lista1, Slownik, first)
		tab2, Lista2, Slownik = przypisz(tab2, Lista2, Slownik, second)

		wygrywa = ''
		if(los == 0):
			print(Slownik)
		elif(los >= 1):
			if((tak_nie() == 'T')):
				print(Slownik)
				continue
			else:
				wygrana = bilans(wygrana,tab1,tab2)
				wygrywa = wynik(wygrana)
				if(wygrywa == 'both'):
					print('Remis ::)')
				else:
					if(wygrywa == 'first'):
						print('Zwycięzca: %s' %first)
					elif(wygrywa == 'second'):
						print('Zwycięzca: %s' %second)

				break		

main()
