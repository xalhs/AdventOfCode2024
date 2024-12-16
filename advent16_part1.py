def mini(a , b , c="NaN"):
	if c == "NaN":
		if a == "NaN":
			if b == "NaN":
				return b
			return b+1
		if b == "NaN" or a+1001<b+1:
			return a+1001
		return b+1
	if a == "NaN":
		if b == "NaN" or c<b+1:
			return c
		return b+1

	if b == "NaN":
		if a+1001<c:
			return a+1001
		return c
	if a+1001<b+1:
		if a+1001<c:
			return a+1001
		return c
	else:
		if b+1<c:
			return b+1
		return c
def min(a,b):
	if a=="NaN":
		return b
	if b == "NaN" or a<b:
		return a
	return b

with open('input16.txt') as fin:
	global map_area
	map_area=[]
	value_area = []
	i=0
	for line in fin:
		map_area.append([])
		value_area.append([])
		j = 0
		for char in line.strip("\n"):
			map_area[i].append(char)
			if char == "S":
				value_area[i].append([0,1000])
			else:
				value_area[i].append(["NaN","NaN"])
			if char == "E":
				final_pos = [i,j]
			j+=1
		i+=1

	import copy
	for k in range(len(map_area)):
		for i in range(len(map_area)-2 , 0 ,-1):
			for j in range(len(map_area[i])):
				if map_area[i][j] == "." or map_area[i][j] == "E" :
					min_left = "NaN"
					min_left = mini(value_area[i][j-1][1] , value_area[i][j-1][0] , value_area[i][j][0])
					min_right = mini(value_area[i][j+1][1] , value_area[i][j+1][0] , value_area[i][j][0])
					min_down = mini( value_area[i+1][j][0] , value_area[i+1][j][1] , value_area[i][j][1])
					min_up = mini(value_area[i-1][j][0] , value_area[i-1][j][1] , value_area[i][j][1])
					value_area[i][j] = [min(min_left , min_right), min(min_up , min_down)]

	prev_value_area = []
	while value_area != prev_value_area:
		prev_value_area = copy.deepcopy(value_area)
		for i in range(len(map_area)-2 , 0 ,-1):
			for j in range(len(map_area[i])):
				if map_area[i][j] == "." or map_area[i][j] == "E" :
					min_left = "NaN"
					min_left = mini(value_area[i][j-1][1] , value_area[i][j-1][0] , value_area[i][j][0])
					min_right = mini(value_area[i][j+1][1] , value_area[i][j+1][0] , value_area[i][j][0])
					min_down = mini( value_area[i+1][j][0] , value_area[i+1][j][1] , value_area[i][j][1])
					min_up = mini(value_area[i-1][j][0] , value_area[i-1][j][1] , value_area[i][j][1])
					value_area[i][j] = [min(min_left , min_right), min(min_up , min_down)]

	min_val = 	min(value_area[final_pos[0]][final_pos[1]][0] , value_area[final_pos[0]	][final_pos[1]][1])
	print(min_val)
