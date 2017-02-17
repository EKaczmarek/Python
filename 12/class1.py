class Bmi:
    def get_data(self):
        self.name = input('Imie: ')
        self.gender = input('Plec Kobieta/Mezczynzna: ')
        self.height = input('Wzrost[cm]: ')
        self.mass = input('Waga: ')
        self.bmi = round(float(int(self.mass) / ((int(self.height)/100)**2)), 2)

    def cat_dog(self):
        self.name = input('Imie: ')
        self.gender = input('Pies / Kot P/K: ')
        self.height = input('Wzrost[cm]: ')
        self.mass = input('Waga: ')
        if(self.gender == 'Pies'):
            self.bmi = round(float(int(self.mass) / ((int(self.height)/100)**2))/1.33, 2)
        elif(self.gender == 'Kot'):
            self.bmi = round(float(int(self.mass) / ((int(self.height)/100)**2))/2.25, 2)

    def display(self):
        print(self.name + " jest: " + self.gender + ", " + str(self.height) 
        + " cm wzrostu" + ", wazy " + str(self.mass) +
         " kg oraz jej bmi wynosi: " + str(self.bmi) + ", stan Twojej wagi to: " 
        + self.norma())
        
    def norma(self):
        if self.gender == 'K':
                self.min = 20
                self.max = 25
                if self.bmi < 16.5:
                    odp = 'Anoreksja :('
                elif (16.5 <= self.bmi < 20):
                    odp = 'Niedowaga'
                elif (20 <= self.bmi < 25):
                    odp = 'Norma'
                elif (25 <= self.bmi < 30):
                    odp = 'Nadwaga'
                elif self.bmi > 30:
                    odp = 'Otylosc'
                
        elif(self.gender == 'M'):     
                self.min = 22.5
                self.max = 27.5
                if self.bmi < 18.5:
                    odp = 'Anoreksja :('
                elif (18.5 <= self.bmi < 22.5):
                    odp = 'Niedowaga'
                elif (22.5 <= self.bmi < 27.5):
                    odp = 'Norma'
                elif (27.5 <= self.bmi < 32.5):
                    odp = 'Nadwaga'
                else:
                    odp = 'Otylosc'
        return odp
        
    def wbmi(self):
        if(person1.bmi < 20):
            self.eat()
            print(self.objext)
        elif(person1.bmi > 25):
            self.move()
            print(self.objext)
        else:
            print('Masz wage w normie')
            
    def aktywnosc(self, przelicznik):
        if(self.bmi < self.min):
            masa = przelicznik * round(self.height, 2)
            ile_schudnac = masa - self.mass
            return ('Powinienes biegac przez ' + str(przelicznik*ile_schudnac) + 
                    ' godzin aby byc w normie.')
        else:
            return('Nie musisz schudnac')
        
    def move(self):
        print('Wybierz swoja aktywnosc \n')
        print('1: Bieganie \n')
        print('2: Jazda na rowerze \n')
        print('3: Uprawianie tanca nowoczesnego \n')
        choice = input()
        if(choice == '1'):
            self.objext = self.aktywnosc(20)
        elif(choice == '2'):
            self.objext = self.aktywnosc(12)
        elif(choice == '3'):
                self.objext = self.aktywnosc(15)
                print(self.objext)

            
    def jedzenie(self, przelicznik):
        if(self.bmi > self.max):
            masa = przelicznik * round(self.height, 2)
            ile_przytyc = masa - self.mass
            return ('Powinienes jesc ' + str(przelicznik*ile_przytyc) + 
                    ' g aby byc w normie.')
        else:
            return('Nie musisz przytyc')
        
    def eat(self):
        print('Wybierz co chcesz jesc \n')
        print('1: Czekolada \n')
        print('2: Chleb \n')
        print('3: Ziemniaki \n')
        choice = input()
        if(choice == '1'):
            self.objext = self.jedzenie(12)
        elif(choice == '2'):
            self.objext = self.jedzenie(60)
        elif(choice == '3'):
            self.objext = self.jedzenie(75)

            
person1 = Bmi()
person1.get_data()
person1.display()
person1.norma()
person1.wbmi()