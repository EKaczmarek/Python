

def range(*args):
	a = 0
	if (len(args) == 1):
		while(a < int(args[0])):
			print (a)
			a +=1
	elif(len(args) == 2):
	  b = int(args[0])
	  while(b < int(args[1])):
	    print(b)
	    b+=1
	elif(len(args) == 3):
	    c = args[0]
	    while(c < int(args[1])):
	        print(c)
	        c+= int(args[2])

range(1,100,3)
input()