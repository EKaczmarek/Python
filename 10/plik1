#size 9,8

plik = ''
dictionary = {}
colory = []
dic = {}


def dict(a, b):
	dict1 = {}
	if(str(lista[a][-1]) == ','):
		dict1['kolor_oczu'] = str(lista[a] + ' ' + lista[a+1])
		dict1['wzrost'] = str(lista[7])
	else:
		dict1['kolor_oczu'] = str(lista[a])
		dict1['wzrost'] = str(lista[b])


	if(dict1['kolor_oczu'] not in colory):
		list = []
		colory.append(dict1['kolor_oczu'])
	
	return dict1

hero_200_plus = open('hero_200_plus.txt', 'w')
hero_short = open('hero_short.txt', 'w')

with open('1.txt', 'r') as file:
	data = 'plik 1.txt'
	while data:
		data = file.readline()
		lista = data.split()
		if not lista:
			continue
		if(lista[3] == 'has'):
			dict1 = dict(4,7)
			if(int(dict1['wzrost']) > 200):
				hero_200_plus.write(str(lista[1] + ' ' + lista[2] + '\n'))       
			else:
				hero_short.write(str(lista[1] + ' ' + lista[2] + '\n'))
			dictionary[str(lista[1] + ' ' + lista[2])] = dict1
		elif(lista[2] == 'has'):
			dict2 = dict(3,6)
			if(int(dict1['wzrost']) > 200):
				hero_200_plus.write(str(lista[1] + '\n'))       
			else:
				hero_short.write(str(lista[1] + '\n'))
			dictionary[str(lista[1])] = dict2
		elif(lista[4] == 'has'):
			dict3 = dict(5,8)
			if(int(dict1['wzrost']) > 200):
				hero_200_plus.write(str(lista[1] + ' ' + lista[2] + ' ' + lista[3] + '\n'))       
			else:
				hero_short.write(str(lista[1] + ' ' + lista[2] + ' ' + lista[3] + '\n'))
			dictionary[str(lista[1])] = dict2

hero_200_plus.close()
hero_short.close()

di = {}
for j in dictionary:
	if dictionary[j]['kolor_oczu'] in colory:
		print(dictionary[j]['wzrost'])
		di[dictionary[j]['kolor_oczu']] = int(dictionary[j]['wzrost'])

print(di)
