# capitalize() title() 1 litera duża
# upper(), lower()
# split tnie na lsite wyrazow
# split('cos') -->usunieccie cos ze sttringa

# strip() -->wycina spacje na koncu i poczatku, 
# ' lalal'.strip().strip('la')
# strip ('ala') usuwa ala 

def pobierz():
  a = str(input('Podaj dowolne zdanie:'))
  list = a.split()
  return list
  
def wyswietl(_list):
  for i in _list:
    if(i.lower() != 'voldemort'):
      print((i).title())
    else :
      print('Sam wiesz kto :)')

  
wyswietl(pobierz())
input()