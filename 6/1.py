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

print('1: ')
print(tekst[35:44])
print('2: ')
print(tekst[64:])
print('3: ')
print(tekst[:34])
print('4: ')
print(tekst[::-1]) # cały napis od tyłu
print('5: ')
print(tekst[:34:4])
print('6: ')
print(tekst[-65:-28])
#string [początek:koniec:krok]

input()

