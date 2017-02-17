class Pitagolas:
    def get_data(self):
        self.przy1 = int(input('Podaj pierwsza przyprostokatna: '))
        self.przy2 = int(input('Podaj druga przyprostokatna: '))
        self.countPrze()
        
    def countPrze(self):
        self.prze = (int((self.przy1**2)+(self.przy2**2))**0.5)
        print("Przeciwprostokatna trojkata o bokach: " + str(self.przy1) + " oraz " + str(self.przy2) + " wynosi " + str(self.prze))
        

triangle = Pitagolas()
triangle.get_data()