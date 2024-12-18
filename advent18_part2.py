def is_map_blocked(map1):
	value_area = [[float('inf') for i in range(size+1)] for j in range(size+1)]
	value_area[starting_pos[0]][starting_pos[1]] = 0
	for k in range(len(map1)):
		for i in range(len(map1)):
			for j in range(len(map1[i])):
				if map1[i][j] == ".":
					min_left = value_area[i][j-1]+1
					min_right = value_area[i][j+1]+1
					min_down =  value_area[i+1][j]+1
					min_up = value_area[i-1][j]+1
					min_cur =  value_area[i][j]
					value_area[i][j] = min(min_left,min_right,min_down,min_up,min_cur)
		if value_area[final_pos[0]][final_pos[1]] != float('inf'):
			return False
			break

	prev_value_area = []
	while value_area != prev_value_area:
		if value_area[final_pos[0]][final_pos[1]] != float('inf'):
			return False
			break
		prev_value_area = copy.deepcopy(value_area)
		for i in range(len(map1)):
			for j in range(len(map1[i])):
				if map1[i][j] == ".":
					min_left = value_area[i][j-1]+1
					min_right = value_area[i][j+1]+1
					min_down =  value_area[i+1][j]+1
					min_up = value_area[i-1][j]+1
					min_cur =  value_area[i][j]
					value_area[i][j] = min(min_left,min_right,min_down,min_up,min_cur)

	if 	value_area[final_pos[0]	][final_pos[1]] == float('inf'):
		return True

def is_map_blocked_for_index(index):
	global line_list
	global size
	blank_map = [["."for i in range(size)] for j in range(size)]
	for line in line_list[:(index+1)]:
		coords = [int(x) for x in  line.rstrip("\n").split(",")]
		blank_map[coords[0]][coords[1]] = "#"

	return 	is_map_blocked(blank_map)

with open('input18.txt') as fin:
	import copy
	global map_area
	global size
	size = 71
	map_area=[["."for i in range(size)] for j in range(size)]
	l=0
	starting_pos = [0,0]
	final_pos = [size-1,size-1]
	map_configs = []
	global line_list
	line_list = []
	for line in fin:
		coords = [int(x) for x in  line.rstrip("\n").split(",")]
		map_area[coords[0]][coords[1]] = "#"
		line_list.append(line.rstrip("\n"))

	min_index = 0
	max_index = len(line_list)-1
	while max_index - min_index > 1:
		next_index = int((min_index+max_index)/2)
		if is_map_blocked_for_index(next_index):
			max_index = next_index
		else:
			min_index = next_index
	if max_index == next_index:
		print(line_list[next_index])
	else:
		print(line_list[next_index+1])
