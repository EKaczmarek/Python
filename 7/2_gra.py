from random import randint

def main():
	while(gra() == "T"):
		continue

def wyjatek():
	try:
		_traf = (input('Zgadnij jaka liczba jest wylosowana :)'))
		return int(_traf)
	except ValueError:
		return 0
		
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

		
def gra():
	a = randint(1,1000)
	print('Wysolowalam: ' + str(a))

	i = 0
	while(i != 5):
		i += 1  
		traf = wyjatek()
		if(traf == 0):
			print("Podales złą liczbe :(")
		if traf < a:
			print('Moja liczba jest większa')
		elif traf > a:
			print('Moja liczba jest mniejsza')
		elif traf == a:
			print('Zgadles! %d to moja liczba' % a)
			break

	return(tak_nie())

main()
input()
