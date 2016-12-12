# try: 
#except: pass NIEEE
# isinstance(tekst(float, int)) --> zwraca bool czy dany tekst jest float lub int


def wyjatki_Liczby(dane):
	if isinstance(dane, int):
		return dane
	try:
		return int(dane)
	except ValueError:
		print("Podales tekst a nie liczbe :(")

def wyjatki_Str(dane):
	dane = str(dane)
	try:
		if dane.isnumeric():
			raise ValueError('')
		return 	str(dane)
	except ValueError:
		print("Podales liczbe a nie tekst :(")

def apka():
	print('Kalkulator BMI dla pan i panow')

	a = 'T'
	while(a != 'N'):
		imie = input('Imie: ')
		_imie = wyjatki_Str(imie)
	
		plec = input('Podaj plec K/M')
		_plec = wyjatki_Str(plec)
	
		w = input('Wzrost: ')
		waga = wyjatki_Liczby(w)

		m = input('Masa: ')
		masa =	wyjatki_Liczby(m)
		
		bmi = float(masa / ((waga/100) **2))
		if bmi < 16.5 and _plec == 'K':
			odp = 'Anoreksja :('
		elif (16.5 <= bmi < 20) and _plec == 'K':
			odp = 'Niedowaga'
		elif (20 <= bmi < 25) and _plec == 'K':
			odp = 'Norma'
		elif (25 <= bmi < 30) and _plec == 'K':
			odp = 'Nadwaga'
		elif bmi > 30 and _plec == 'K':
			odp = 'Otylosc'
		
		elif bmi < 18.5 and _plec == 'M':
			odp = 'Anoreksja :('
		elif (18.5 <= bmi < 22.5) and _plec == 'M':
			odp = 'Niedowaga'
		elif (22.5 <= bmi < 27.5) and _plec == 'M':
			odp = 'Norma'
		elif (27.5 <= bmi < 32.5) and _plec == 'M':
			odp = 'Nadwaga'
		else:
			odp = 'Otylosc'
		
		if(_plec == 'K'):
			p = 'kobiety'
		elif(_plec == 'M'):
			p = 'mezczyzny'
		
		DataBase = {imie,w,m,plec,odp}
		
		try:
			a = input('Czy liczyc dla nastepnej osoby T -->Tak, N --> Nie')
		except:
			print("Wpisz 'T' lub 'N'")

		from pprint import pprint as pp
		pp(DataBase)

apka()
input()
