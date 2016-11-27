print('Kalkulator BMI')
wzrost = float(input('Wzrost: '))
masa = float(input('Masa: '))
p = raw_input('Plec: ')
bmi = masa / ((wzrost/100) **2)
if bmi < 20.0:
	odp = 'Niedowaga'	
elif 20.0 <= bmi <= 25.0:
	odp = 'Norma'	
elif bmi > 25.0:
	odp = 'Nadwaga'
print('BMI wynosi: ' + str(bmi) + '\n' + odp)
raw_input();