with open('input6.txt') as fin:
	line_list = []
	
	map_area = []
	i=0
	for line in fin:
		map_area.append(line.rstrip("\n")+"$")
		if "^" in line:
			starting_pos = [i,line.index("^")]
	
		i+=1
	map_area.append("$"*len(map_area[-1]))
	cur_pos = starting_pos	
	inside = True
	sum = 1
	up = 1
	right = 0
	pos_visited = [cur_pos]
	while inside:
		next_tile = map_area[cur_pos[0] - up ][ cur_pos[1] +right]
		if next_tile =="$":
			break
		elif next_tile =="." or next_tile =="^" :
			cur_pos = [cur_pos[0] - up , cur_pos[1] +right]
			if cur_pos not in pos_visited:
				sum+= 1
				pos_visited.append(cur_pos)
		elif next_tile == "#":
			temp = right
			right = up
			up = -temp	
			 
	print(sum)
