from random import randrange
def myName():
    return "JUAN"
def column(grid:list, disc:str) -> int:
	discs = 0   
	for i in range(6):
		for j in grid[i]:
			if j == disc:
				discs += 1
	if discs % 2 == 0:
		c = 0
	else:
		c = 1
	return c 
			
