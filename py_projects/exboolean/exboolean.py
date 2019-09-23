#Works, but inefficient
m=int(input('Enter your mark: '))
if m < 0:
	print('Mark is not valid')
elif m < 5:
	print('Fail')
elif m <= 6:
	print('Good')
elif m <= 8:
	print('Quite good')
elif m <= 10:
	print('Astonishing')
else:
	print('Mark is not valid')

