file = open(name [,access_mode])

file = 'ścieżka'
access_mode = {'r', 'w', 'a', 'rb', 'wb'}
data = file.read()

data = file.readLine()
data = file.readLines()
#write -->string
#writeLines -->liste stringów

with open('plik', 'w') as file:
	file.write('lalla') --> wyjscie z konteksty

file.close()