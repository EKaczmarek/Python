import json

class Tasks:
    
    def zapis(self):
        self.family = list()
        self.family_cat = list()

        while(True):
            while(True):
                    self.k = input('Podaj klucz: ' )
                    self.v = input('Podaj wartosc: ')
                    self.x = {(self.k): (self.v)}
                    self.a = input('Czy podajesz nowe kryterium? T/N: ')
                    self.family_cat.append(self.x)
                    if(self.a == 'N'):
                        self.temp = self.family_cat
                        self.family.append(self.temp)
                        break
                    else:
                        continue
            self.a = input('Czy podajesz nowego czlonka rodziny? T/N: ')
            if(self.a == 'N'):
                with open ('class3.txt', 'w') as file:
                    json.dump(self.family, file)
                    break
            else:
                continue
    def odczyt(self):
        print('Podales nastepujace dane: \n')
        from pprint import pprint as p
        with open('class3.txt', 'r') as file:
            data = json.load(file)
        p(data)
        
    def menu4(self):
        while(True):
            print('Wybierz opcję: \n')
            print('1: Dodaj do pliku \n')
            print('2: Wczytaj z pliku \n')
            print('3: Sprawdz stan rodziny \n')
            print('4: Wyjscie \n')
            try:
                self.choice = input()
                if(self.choice == '1'):
                    self.zapis()
                elif(self.choice == '2'):
                    self.odczyt()
                elif(self.choice == '3'):
                    self.odczyt()
                elif(self.choice == '4'):
                    break
            except:
                print('Sprobuj jeszcze raz :) \n')
                self.menu()
                       
            
Kamalek = Tasks()
Kamalek.menu4()
