def square(a: float) -> float:
	return a*a

def triangle(b: float, h: float) -> float:
	return b*h/2

def circle(r: float) -> float:
	import math	
	return round(math.pi*math.pow(r, 2),2)

if __name__ == '__main__':
	figure = int(input('Select a geometrical figure (1-Square, 2-Triangle, 3-Circle): '))
	if figure == 1:
		print(square(float(input('Enter side: '))))
	elif figure == 2:
		b = float(input('Enter base: '))
		h = float(input('Enter height: '))
		print(triangle(b, h))
	elif figure == 3:
		print(circle(float(input('Enter radius:'))))
	else:
		print('Wrong input, terminating program')
		
