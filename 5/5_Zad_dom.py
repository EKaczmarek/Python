motto = "The Zen of Python, by Tim Peters. Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those!"


list = []
list = motto.split('. ')

def first():
  print('Zdania ze słowem "is": ')
  for i in list:
    if i.find("is") != -1:
      print(i)
 
def second():
  print('Zdania złożone z przecinkiem: ')
  for i in list:
    if i.find(",") !=-1:
      print(i)

def third():
	list1 = []
	list1 = motto.split()
	k = -1
	for i in list1:
		k+=1
		if (i.istitle() == True):
			list1[k] = 'Python'
	print(list1)

third()
