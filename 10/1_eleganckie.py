list_of_dicts = list()

def first():
	with open('1.txt', 'r') as file:
		line = file.readline().split()
		while(1):
			name = ''
			end_of_name = (line.index('has') if 'has' in line else None)
			end_of_eyes = (line.index('and') if 'and' in line else None)

			if(line):
				for i in range(1, end_of_name):
					if line[i] != 'has':
						name += (line[i])
						name += ' '
				if(line[end_of_name + 4].isdigit() == True):
					eyes = line[end_of_name + 1]
					height = line[end_of_name + 4]
				else:
					for i in range(end_of_name + 1, end_of_eyes):
						if line[i] != 'and':
							eyes += line[i]
							eyes += ''
					height = line[end_of_eyes + 2]

				list_of_dicts.append({name : 
					{'kolor oczu':eyes ,
					 'wzrost':  height}})
				eyes = ''
				height = ''
				line = file.readline().split()
			else:
				break

		
def second():
	with open('hero_200_plus.txt', 'w') as tall, open('hero_Short.txt', 'w') as short:
		for i in list_of_dicts:
			for j in i:
				if(int(i[j]['wzrost']) > 200):
					print(i[j]['wzrost'])
					tall.write(j)
					tall.write("\n")
				else:
					short.write(j)
					short.write("\n")
		
first()
second()
