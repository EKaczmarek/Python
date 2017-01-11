class Figura:
	"Pierwsza klasa"
	def __init__(self, x, y):
		self.x = x
		self.y = y
	def info(self):
		print(self.x, self.y)
	def zmien(self, x, y):
		self.x = x
		self.y = y

o = Figura(1, -1)
o.info()
o.zmien(10,11)
o.info()