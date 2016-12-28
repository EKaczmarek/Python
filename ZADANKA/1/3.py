slownikCyfr = {1:"jeden", 2:"dwa", 3: "trzy", 4: "cztery", 5:"pięć", 6:"sześć", 
                  7: "siedem", 8:"osiem", 9:"dziewięć"}
slownikDwucyfr = {10: "dziesięć", 11:"jedenaście",
                  14:" czternaście", 15: " piętnaście", 16: " szesnaście", 19: " dziewiętnaście",
                  20:" dwadzieścia", 30:" trzydzieści", 40: " czterdzieści", 50:" pięćdziesiąt", 
                  60: " sześćdziesiąt", 70:" siedemdziesiąt", 80:" osiemdziesiąt", 
                  90:" dziewięćdziesiąt"}
slownikTrzyCyfr = {100:"sto", 200:"dwieście", 300:"trzysta", 400:"czterysta", 
					500:"pięćset", 600:"sześćset", 700:"siedemset", 800:"osiemset",900:"dziewięćset"}
                  #oprocz 11,12,13,17,18

def dwuCyfr(n):
	if n in slownikDwucyfr:
		return (slownikDwucyfr[n])
	elif (str(n)[0] == "1"):
		return ("%snaście" %slownikCyfr[n%10])
	else:
		return (slownikDwucyfr[int(n/10) * 10] + " " + slownikCyfr[n%10])
		
def trzyCyfr(n):
	liczba = ''
	if (len(str(n)) == 1):
		liczba += (slownikCyfr[n])
	elif (len(str(n)) == 2):
		liczba += (dwuCyfr(n))
	elif (len(str(n)) == 3):
		print(len(slownikTrzyCyfr(n)))
		liczba += (slownikTrzyCyfr[int(n/100) * 100])
		liczba += (dwuCyfr(int(n%100)))
	return liczba
		
def slownie(n):
	liczba = ''
	print(len(str(n)))
	
	if(len(str(n)) <= 3):
		liczba = (trzyCyfr(n))
		
	elif((len(str(n)) > 3) and  (len(str(n)) <= 6)):
		liczba = trzyCyfr(int(n/1000))
		if(int(n/1000) == 1):
			liczba += " tysiąc "
			liczba +=trzyCyfr(int(n%1000))
		elif(int(str(n)[4]) > 1 and int(str(n)[4]) < 5):
			liczba +=" tysiące "
			liczba +=trzyCyfr(int(n%1000))
		elif(int(str(n)[4]) > 4):
			liczba +=" tysięcy "
			liczba +=trzyCyfr(int(n%1000))
			
	elif(len(str(n)) >= 7):
		liczba = trzyCyfr(int(n/1000000))
		if(int(n/1000000) == 1):
			liczba += " milion "
			print(int(n/1000) - int(n/1000000)*1000)
			liczba +=trzyCyfr(int(n/1000) - int(n/1000000)*1000)
		elif(int(n/1000000) > 1 and int(n/1000000) < 5):
			liczba +=" miliony "
			print(int(n/1000) - int(n/1000000)*1000)
			liczba +=trzyCyfr(int(n/1000) - int(n/1000000)*1000)
		elif(int(n/1000000) > 4 and int(n/1000000) < 1000):
			liczba +=" milionów "
			liczba +=trzyCyfr(int(int(n/1000) - int(n/1000000)*1000))
		
		if(int(n/1000) == 1):
			liczba += " tysiąc "
			liczba +=trzyCyfr(int(n%1000))
		elif(int(str(n)[4]) > 1 and int(str(n)[4]) < 5):
			liczba +=" tysiące "
			liczba +=trzyCyfr(int(n%1000))
		elif(int(str(n)[4]) > 4):
			liczba +=" tysięcy "
			liczba +=trzyCyfr(int(n%1000))
	print(liczba)
	  

def main():
	slownie(39942105)

main()
input()

