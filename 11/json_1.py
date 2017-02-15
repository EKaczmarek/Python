import json
import sys
sys.getdefaultencoding()

from pprint import pprint
with open('py_10_2.txt','r') as data_file:    
    data = json.load(data_file)
pprint(data)

with open('women.txt', 'w') as women, open('men.txt', 'w') as men:
    for i in data:
        if(i['gender'] == 'male'):            
           json.dump(i['name'], men)
        elif(i['gender'] == 'female'):
           json.dump(i['name'], women)
           
with open('sw_all_heros.txt', 'w') as heros:
    for i in data:
        if(i['mass'] != 'unknown'):
            line = i['name'] + " wazy " + i['mass'] + " kg, jest ";
            if(i['gender'] == 'male'):            
                line += " mezczyzna "
            elif(i['gender'] == 'female'):
                line += " kobieta "
            else:
                line = ""
            if(line != ""):
                line += " i jego rok urodzenia to: " + i['birth_year']
                json.dump(line, heros)
                heros.write('\n')
                line = ""
    

