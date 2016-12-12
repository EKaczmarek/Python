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
	DataBase = []
	Dict = {}
	a = 'T'
	while(a != 'N'):
		i = input('Imie: ')
		imie = wyjatki_Str(i)
	
		p = input('Podaj plec K/M')
		plec = wyjatki_Str(p)
	
		w = input('Wzrost: ')
		wzrost = wyjatki_Liczby(w)

		m = input('Masa: ')
		masa =	wyjatki_Liczby(m)
		
		bmi = float(masa / ((wzrost/100) **2))
		if bmi < 16.5 and plec == 'K':
			odp = 'Anoreksja :('
		elif (16.5 <= bmi < 20) and plec == 'K':
			odp = 'Niedowaga'
		elif (20 <= bmi < 25) and plec == 'K':
			odp = 'Norma'
		elif (25 <= bmi < 30) and plec == 'K':
			odp = 'Nadwaga'
		elif bmi > 30 and plec == 'K':
			odp = 'Otylosc'
		
		elif bmi < 18.5 and plec == 'M':
			odp = 'Anoreksja :('
		elif (18.5 <= bmi < 22.5) and plec == 'M':
			odp = 'Niedowaga'
		elif (22.5 <= bmi < 27.5) and plec == 'M':
			odp = 'Norma'
		elif (27.5 <= bmi < 32.5) and plec == 'M':
			odp = 'Nadwaga'
		else:
			odp = 'Otylosc'
		
		if(plec == 'K'):
			p = 'Kobieta'
		elif(plec == 'M'):
			p = 'Mężczyzna'
		
		Dict = {'imie':imie, 'waga':wzrost, 'masa':masa, 'plec': p, 'Status wagi': odp }
		DataBase.append(Dict)
		
		try:
			a = input('Czy liczyc dla nastepnej osoby T -->Tak, N --> Nie')
		except:
			print("Wpisz 'T' lub 'N'")

		from pprint import pprint as pp
		pp(DataBase)

apka()
