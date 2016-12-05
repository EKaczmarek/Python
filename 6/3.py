tekst = """The Zen of Python, by Tim Peters
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
	list = []
	list = tekst.split()
	a = 0
	flaga = 0

	for i in list:
		a += 1
		if i.endswith(',') == True:
		  flaga = 1
		while(flaga == 1):
			if i.endswith('.') == False:
				print(list[a])
			elif i.endswith('.') == True:
				print(list[a])
				flaga = 0
			a+=1

zad1()
input()