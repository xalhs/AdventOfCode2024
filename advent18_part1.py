with open('input18.txt') as fin:
	global map_area
	size = 71
	map_area=[["."for i in range(size)] for j in range(size)]
	i=0
	starting_pos = [0,0]
	final_pos = [size-1,size-1]
	value_area = [[float('inf') for i in range(size+1)] for j in range(size+1)]
	for line in fin:
		if i == 1024:
			break
		coords = [int(x) for x in  line.rstrip("\n").split(",")]
		map_area[coords[0]][coords[1]] = "#"
		i+=1
	value_area[starting_pos[0]][starting_pos[1]] = 0
	import copy
	for k in range(len(map_area)):
		for i in range(len(map_area)):
			for j in range(len(map_area[i])):
				if map_area[i][j] == ".":
					min_left = value_area[i][j-1]+1
					min_right = value_area[i][j+1]+1
					min_down =  value_area[i+1][j]+1
					min_up = value_area[i-1][j]+1
					min_cur =  value_area[i][j]
					value_area[i][j] = min(min_left,min_right,min_down,min_up,min_cur)

	prev_value_area = []
	while value_area != prev_value_area:
		prev_value_area = copy.deepcopy(value_area)
		for i in range(len(map_area)):
			for j in range(len(map_area[i])):
				if map_area[i][j] == ".":
					min_left = value_area[i][j-1]+1
					min_right = value_area[i][j+1]+1
					min_down =  value_area[i+1][j]+1
					min_up = value_area[i-1][j]+1
					min_cur =  value_area[i][j]
					value_area[i][j] = min(min_left,min_right,min_down,min_up,min_cur)

	min_val = 	value_area[final_pos[0]	][final_pos[1]]
	print(min_val)
