import re

def ugly(a):
	lista = [2,3,5]
	if(a == 1):
		return True
	for i in lista:
		if(a % i == 0):
			return True
	return False

def get_time(amount, what):
	list = []
	list = re.findall('\d+', amount)
	list = map(int, list)
	print(float(list[1]/60))

	if(what == 's'):
		return(list[0]*3600 + list[1]*60 + list[2])
	elif(what == 'm'):
		return (list[0]*60 + list[1] + float(list[2]/60))
	elif(what == 'h'):
		return (list[0] + list[1]/float(60) + list[2]/float(360))

def flatten(list):
	print('dupa')

def validate_email(email):
	if(email[-7:] == '@com.pl'):
		return True
	else:
		return False

def validate_zip(zip):
	digit = False
	list = re.findall('\d+', zip)
	if(len(list[0]) == 2 and len(list[1]) == 3):
		digit = True
	if((len(zip) == 6) and (zip[2] =='-') and digit == True):
		return True
	else:
		return False

def arb_2_rom(a):
	slownik = {1: 'I',5:'V', 10:'X', 50:'L',100:'C',500:'D',1000:'M' }
	for i in slownik:
		if (a / i > 1):
			print(slownik[i])

def longest_word(sentence):
	list = sentence.split()
	print(list)
	longest = list[0]
	for i in list:
		if(len(i) > len(longest)):
			longest = i
	return longest

print("Powtorka :)")
a = input("Ktore zadanie wyswietlic? ")
if(a == 1):
	print("ugly(12) = " + str(ugly(12)))
	print("ugly(11) = " + str(ugly(11)))
	print("ugly(1) = " + str(ugly(1)))
elif(a == 2):
	a = raw_input('podaj godzine w formacie hh:mm:ss')
	print(str(a) + ' = ' + str(get_time('2:00:00', 's'))+ ' seconds')
	print(str(a) + ' = ' + str(get_time('12:00:00', 'm')) + ' minutes')
	print(str(a) + ' = ' + str(get_time('1:15:00', 'h')) + ' hours')
elif(a == 3): #chwilowo zawieszone
	print(flatten([[[[[[[[],'a'],'b']]]],'c']]))
elif(a == 4):
	name = raw_input('Podaj email do sprawdzenia ')
	print(name + " " + str(validate_email(name))
	zip = raw_input('Podaj kod pocztowy do sprawdzenia')
	print(zip + " " + str(validate_zip(zip)))
elif(a == 5): #chwilowo zawieszone
	print(arb_2_rom(123))
elif(a == 6):
	print(longest_word('lalalal gt pol blala Rafaulek'))




