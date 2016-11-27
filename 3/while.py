print('Kalkulator BMI dla pan i panow')

a = 'T'
while(a != 'N'):

		w = float(input('Wzrost: '))
	m = float(input('Masa: '))
	plec = str(input('Podaj plec K/M'))

	print('LOL')
		
	bmi = (m / ((w/100) **2))

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
		p = 'kobiety'
	elif(plec == 'M'):
		p = 'mezczyzny'

	
	a = input('Czy liczyc dla nastepnej osoby T -->Tak, N --> Nie')

