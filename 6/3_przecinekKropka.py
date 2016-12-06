tekst = """The Zen of Python, by Tim Peters.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
"""

def zad1():
	flag = 0
	napis = ' '
	for i in tekst:
		if i == ',':
			flag = 1
		elif i != ',' and i != '.' and flag == 1:
			napis= napis.join(i)
			print(napis)
		elif i == '.' and flag == 1:
			flag = 0
			print(napis)

def zad1listy():
	a = 0
for i in tekst:
	a+=1
	if tekst[a] == ',':
		while tekst[a] != '.':
			a += 1
			print(tekst[a])


def zad2():
	lista = tekst.split()
	a = 0
	for i in lista:
		a+=1
		if i == 'is':
		print(lista[a])


def zad3():
	lista = tekst.split()
	a = 0
	for i in lista:
		a+=1
		if i == 'is':
			k = a
			while tekst[k] != ' ':
				k-=1
