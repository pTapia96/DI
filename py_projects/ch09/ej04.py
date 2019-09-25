alkaline_earth_materials = [[4, 9.012], [12, 24.305], [20, 40.078], [38, 87.62], [56, 137.327], [88, 226]]
number_and_weight = []

for i in alkaline_earth_materials:
	print(i[0])
	print(i[1])
	number_and_weight.append(i[0])
	number_and_weight.append(i[1])

print(list(number_and_weight))
