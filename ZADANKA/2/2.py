from HTMLParser import HTMLParser

# create a subclass and override the handler methods
#class object(object):
	#"Pierwsza klasa"
class object1:
	def __init__(self,x,y):
		self.a = x
		self.b = y
		print("Stworzenie klasy Object!! :)")

class HtmlObject(object1):
	def __init__(self, x, y):
		self.a = x
		self.b = y
		print("Stworzenie klasy HtmlObject!! :)")
	def html(self):
		s = """<html>
\t<head>	
\t\t<title>Test</title>
\t</head>
\t<body>
\t\t<h1> x = """ + str(self.a) + ", y = " +  str(self.b) + """"
\t\t</h1>
\t</body>
</html>"""
		plik = open('html2.txt', 'w')
		plik.write("lol")
		plik.close()
		return s

# instantiate the parser and fed it some HTML
strona = HtmlObject(1,2)
print(strona.html())
input()