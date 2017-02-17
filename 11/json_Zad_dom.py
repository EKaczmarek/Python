import json

from pprint import pprint
with open('py_10_zd.txt','r') as data_file:    
    data = json.load(data_file)
pprint(data)

with open('ships.txt', 'w') as ships:
    my_list = [a for a in data if a['cost_in_credits'] != 'unknown']
    my_list_2 = sorted(my_list, key = lambda x: int(x['cost_in_credits']), reverse = True)
    for i in my_list_2:
        line = i['name'] + " kosztuje " + i['cost_in_credits'] + " credits.\n"
        ships.write(line)


