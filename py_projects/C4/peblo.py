from random import randrange
def myName():
    return "PABLO"

def is_legal(c:int, grid:list) -> bool:
	legal = True	
	illegal_cs = [14]
	
	count = -1	
	for i in grid[6]:
		count += 1
		if i == -1:
			illegal_cs.append(count)
	for i in illegal_cs:
		if c == i:
			legal = False
	return legal

def column(grid:list, disc:str) -> int:
	c = randrange(0, 9, 1)
	
	flag = 0	
	while flag == 0:
		if is_legal(c, grid) == True:
			flag = 1
		else:
			c = randrange(0, 9, 1)
	return c
