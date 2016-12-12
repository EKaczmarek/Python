import random

def gra():
	print('Gra wisielec')
	lista = ['lekkoatletyka','interpunkcja', 'telekomunikacja', 'penis', 'żółć', 'kolorowanka', 'antyterrorysta']

	counter = 0
	word = (random.choice(lista))
	print(word)
	win = False
	print(len(word) * '*')
	res = len(word) * '*'

	while(win == False):
		shot = str(input('Zgaduj zgadula jaki mamy wyraz : '))
		counter += 1
		if len(shot) == 1:
			if(word.find(shot) >= 0):
				res = (findLetter(res,shot,word))
				print(res)
			elif(word.find(shot) < 0):
				print(result)
				
			if (full(res, word) == True):
				print("Wygrałeś - ilość tur %d" %counter)
				win = True
				break

		elif(len(_shot) == len(_word)):
			if(_shot == _word):
				print("Wygrałeś - ilość tur %d" %counter)

				win = True	
			else:
				print("Probuje dalej ")

def findLetter(_res,_shot, _word):
	res = ''
	k = 0
	for i in _word:
		if i ==_shot and _res[k] =='*':
			res += str(i)
		elif i ==_shot and _res[k] == i:
			res = str(_res)
			break
		if i != _shot and _res[k] == '*':
			res += '*'
		elif i != _shot and _res[k] != '*':
			res += str(_res[k])
		k += 1

	return res		

def full(_res, _word):
	if _res == _word:
		return True
	else:
		return False

gra()
