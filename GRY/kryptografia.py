print(bin(256))

def wyjatek():
	try:
		_traf = (input('Podaj klucz (liczbe od 0 do 255) '))
		return int(_traf)
	except ValueError:
		return -1

def tekst():
	try:
		output = str(input('Podaj tekst do zaszyfrowania')) 
		if output.isnumeric() == True:
			raise ValueError('')
		else:
			return output
	except ValueError:
		tekst()
def toBinary(_list):
	list = []
	for i in _list:
		list.append(bin(i))
	return list

def zaszyfruj(tekst, klucz):
	list = []
	[list.append(ord(c)) for c in tekst]

	list = toBinary(list)
	print(list)

	listBin = []
	for i in list:
	  print(8 ^ 15)
		#listBin.append((i ^ bin(klucz)))

	return listBin


def main():
	k = -1
	while (k == -1):
		k = wyjatek()
	print(bin(k))

	szyfr = tekst()
	print(zaszyfruj(szyfr, k))



main()
input()