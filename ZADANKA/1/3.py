def slownie(n):
	print(len(str(n)))
	slownikCyfr = {1:"jeden", 2:"dwa", 3: "trzy", 4: "cztery", 5:"pięć", 6:"sześć", 
                  7: "siedem", 8:"osiem", 9:"dziewięć"}
	slownikDwucyfr = {10: "dziesięć", 11:"jedenaście"
                  14:"czternaście", 15: "piętnaście", 16: "szesnaście", 19: "dziewiętnaście"}
                  #oprocz 11,12,13,17,18
	slownikReszta = {20:"dwadzieścia", 30:"trzydzieści", 40: "czterdzieści" }
	#, 50:"pięćdziesiąt", 60: "sześćdziesiąt", 70:"siedemdziesiąt", 80:"osiemdziesiąt", 90:"dziewięćdziesiąt" }

	if(n in slownikDwucyfr):
		print(slownikDwucyfr[n])
	elif(n in slownikCyfr):
		print(slownikCyfr[n])
  
def main():
	slownie(152365)

main()

