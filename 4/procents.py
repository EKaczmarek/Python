DataBase={'Waga','Wzrost'}

def fkcja1():
	waga = float(input('Waga: '))
	wzrost = float(input('Wzrost'))
	DataBase = {'Waga' : waga, 'Wzrost': wzrost}
	return DataBase

def fkcja2(DataBase):
		print(DataBase)
		BMI(DataBase)

def BMI(DataBase):
  	bmi = (DataBase['Waga'] / ((DataBase['Wzrost'] /100) **2))
  	print('Twoje bmi %2.2f. ' % bmi)
  	if(bmi<20): 
  	 print('Niedowaga.')
  	elif(20<=bmi<=25):
  	  print('Norma.')
  	elif(bmi>25):
  	  print('Nadwaga.')

fkcja2(fkcja1())
