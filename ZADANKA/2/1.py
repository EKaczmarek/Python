
from random import randint

def rzut_kostka():
	return randint(1,6)

def wyj_imie():
	try:
		imie = ''
		imie = (input('Podaj imie gracza'))
		if imie.isnumeric() == True:
			raise ValueError('')
		else:
			return imie
	except ValueError:
		print('Podales zle imie gracza')
		return 0


def bilans(_wygrana, tab1, tab2):
  
	if(int(tab1[0] + tab1[1]) > int(tab2[0]+tab2[1])):
		_wygrana.append('first')
	elif(int(tab1[0] + tab1[1]) < int(tab2[0]+tab2[1])):
		_wygrana.append('second')
	elif(int(tab1[0] + tab1[1]) == int(tab2[0]+tab2[1])):
		_wygrana.append('both')

	print(_wygrana)
	return _wygrana

def wynik(_wygrana):
	if(int(_wygrana.count('first')) > int(_wygrana.count('second'))):
		print('first')
		return 'first'
	elif(int(_wygrana.count('first')) < int(_wygrana.count('second'))):
		print('second')
		return 'second'
	elif(int(_wygrana.count('first')) ==  int(_wygrana.count('second'))):
		print('both')
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

	#pierwszy gracz
	first = wyj_imie()
	while(first == 0):
		first = wyj_imie()
	#drugi gracz
	second = wyj_imie()
	while(second == 0):
		second = wyj_imie()

	n = int(input('Ile tur chcecie rozegrac?'))
	tura = 0
	while(tura < n):
		tura += 1
		tab1, Lista1, Slownik = przypisz(tab1, Lista1, Slownik, first)
		tab2, Lista2, Slownik = przypisz(tab2, Lista2, Slownik, second)

		wygrywa = ''
		print(Slownik)
		wygrana = bilans(wygrana,tab1,tab2)
		

	wygrywa = wynik(wygrana)
	if(wygrywa == 'both'):
			print('Remis ::)')
	else:
		if(wygrywa == 'first'):
			print('Zwyciezca: %s' %first)
		elif(wygrywa == 'second'):
			print('Zwyciezca: %s' %second)


main()
input()