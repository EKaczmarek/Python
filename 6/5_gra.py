from random import randint

def gra():
	a = randint(1,1000)
	print('Wysolowalam: ' + str(a))
  
	i = 0
	while(i != 5):
		i += 1  
		traf = int(input('Zgadnij jaka liczba jest wylosowana :)'))
		if traf < a:
			print('Moja liczba jest większa')
		elif traf > a:
			print('Moja liczba jest mniejsza')
		elif  traf == a:
			print('Zgadles! %d to moja liczba' % a)
			break
	return str(input('czy chcesz grac jeszcze raz T/N?')) 
  
while(gra() == 'T'):
	continue
