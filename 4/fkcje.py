def data():
	a = str(input('Imie'))
	b = str(input('Nazwisko'))
	w = int(input('wiek'))

	dane = 'Siema jestem %s %s ,mam %2.0f lat'
	wynik = dane % (a,b,w)
	
print(wynik) 