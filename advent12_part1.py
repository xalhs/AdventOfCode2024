import copy

def check_neighbors(i,j):
	letter =copy.copy(map_area[i][j])
	area = 1
	connections = 0
	map_area[i][j] = "1"
	if map_area[i+1][j] == letter:
		answer = check_neighbors(i+1 , j )
		area += answer[0]
		connections += answer[1]
	elif map_area[i+1][j] == "1":
		connections +=1	
	if map_area[i-1][j] == letter:
		answer = check_neighbors(i-1 , j )
		area += answer[0]
		connections += answer[1]
	elif map_area[i-1][j] == "1":
		connections +=1			
	if map_area[i][j+1] == letter:
		answer = check_neighbors(i , j+1 )
		area += answer[0]
		connections += answer[1]
	elif map_area[i][j+1] == "1":
		connections +=1	
	if map_area[i][j-1] == letter:
		answer = check_neighbors(i , j-1 )
		area += answer[0]
		connections += answer[1]	
	elif map_area[i][j-1] == "1":
		connections +=1	
	
	map_area[i][j] = "0"
	return [area,connections]			

with open('input12.txt') as fin:
	global map_area
	global regions_area
	global regions_connections
	region_index = -1
	regions_area = []
	regions_connections = []
	map_area=[]
	i=0
	for line in fin:
		map_area.append([])
		for char in line.strip("\n"):
			map_area[i].append(char)
		map_area[i].append("0")	

		i+=1
	map_area.append(["0"]*len(map_area[-1]))
	
	for i in range(len(map_area)):
		for j in range(len(map_area[0])):
			if map_area[i][j] != "0":
				region_index +=1
				answer = check_neighbors(i,j)
				regions_area.append(answer[0])
				regions_connections.append(answer[1])
						
	sum = 0
	for index in range(len(regions_area)):
		sum += regions_area[index]*(4*regions_area[index] - 2 *regions_connections[index])
		
	print(sum)
