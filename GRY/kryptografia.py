import binascii

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

def zaszyfruj(tekst, klucz):
	list = []
	[list.append(ord(c)) for c in tekst]

	listBin = []
	for i in list:
		listBin.append(bin(i ^ klucz))

	listzaszyfr = []
	[listzaszyfr.append(chr(int(d, 2))) for d in listBin]
	
	zaszyfr = ''.join (listzaszyfr)
	return zaszyfr

def main():
	k = -1
	while (k == -1):
		k = wyjatek()
	print(bin(k))

	szyfr = tekst()
	print(zaszyfruj(szyfr, k))

main()
