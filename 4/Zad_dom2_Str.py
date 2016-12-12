def pobierz():
  a = str(input('Podaj dowolne zdanie:'))
  list = a.split()
  return list
  
def wyswietl(_list, _dict):
  	for i in _list:
	    if i.lower() in _dict.keys():
	    	print(_dict[i.lower()])
	    	break
	    else:
	    	print((i).title())

dicton = { 'voldemort': 'Sam-wiesz-kto...RUN BITCH!!RUN!',
			'zimny': 'walkingDead',
			'bękart' :'graTron'
}
wyswietl(pobierz(), dicton)
input()