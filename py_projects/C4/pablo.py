from random import randrange
def myName():
    return "PABLO"

#def roll(illegal_n:list) -> int:
#	flag = 0	
#	while flag == 0:
#		n = randrange(0, 9, 1)
#		for i in illegal_n:
#			if n == i:
#				flag = 0
#			else:
#				flag = 1

def column(grid:list, disc:str) -> int:
	illegal_c = [14]
	c = 0
	count = -1	
	for i in grid[6]:
		count += 1
		if i == -1:
			illegal_c.append(count)
			print("Añadido a lista negra", count)
	flag = 0	
	while flag == 0:
		flag = 0
		for i in illegal_c:
			if c == i:
				c += 1
				print("Más uno loco")
			elif c != i:
				print("Palante")
				flag = 1
	return c
