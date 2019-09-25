whales = [5, 4, 7, 3, 2, 3, 2, 6, 4, 2, 1, 7, 1, 3]
more_whales = []
for i in whales: #esto es para recorrer el contenido de una lista
#for i in range(len(whales)): #esto es para recorrer el índice de una lista
	more_whales.append(i+1)	
	#more_whales.append(whales[i]+1)
print(list(more_whales))
