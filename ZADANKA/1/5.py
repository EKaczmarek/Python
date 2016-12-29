import sys

def tabliczka(x1, x2, y1, y2):
	i = x1
	k = y1
	listax= dolisty(x1,x2)
	listay= dolisty(y1,y2)
	print("", end = "\t")
	for i in listax:
		print(str(i), end = "\t")

	kolumna = 0
	print("\n")
	for k in listay:
		for i in listax:
			if(kolumna == 0):
				print(k, end = "\t")
			print(i * k , end = "\t")
			kolumna += 1
		kolumna = 0
		print("\n")

def dolisty(a1, a2):
	listax = []
	i = a1
	while(i != a2+1):
		listax.append(i)
		i+=1
	return listax

tabliczka(1,10,2,4)
input()