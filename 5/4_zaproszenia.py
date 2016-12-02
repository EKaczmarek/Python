x = {
	'Ela':{
	'imie': 'Aurelia', 
	'nazwisko':'Kaczmarek' ,
	'wiek': 22,
	'numerButa': 40
	},
	'Amelia':{
	'imie': 'Amelia', 
	'nazwisko':'Matysek',
	'wiek': 24,
	'numerButa': 38
	}
}

print(x)

for i in x:
	a = 'Sz.P {0} {1} {3} chciałabym Ciebie zaprosić na moje urodziny na których będę stawiać {2} tort'.format(*x)
	print(a)

