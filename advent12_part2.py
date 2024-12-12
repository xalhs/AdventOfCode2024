import copy

def check_neighbors(i,j):
	letter =copy.copy(map_area[i][j])
	area = 1
	connections = 0
	neighbors = 0 
	vertices = 0
	map_area[i][j] = "1"
	vert = 0
	hor = 0
	up = 0
	down = 0
	right = 0
	left = 0
	if map_area[i+1][j] == letter:
		answer = check_neighbors(i+1 , j )
		area += answer[0]
		vertices += answer[1]
		neighbors += 1
		down = 1
		vert +=1
	elif map_area[i+1][j] == "1":
		connections +=1
		neighbors += 1	
		down = 1
		vert +=1
	if map_area[i-1][j] == letter:
		answer = check_neighbors(i-1 , j )
		area += answer[0]
		vertices += answer[1]
		neighbors += 1
		up = 1
		vert +=1
	elif map_area[i-1][j] == "1":
		connections +=1		
		neighbors += 1	
		up = 1
		vert +=1
	if map_area[i][j+1] == letter:
		answer = check_neighbors(i , j+1 )
		area += answer[0]
		vertices += answer[1]
		neighbors += 1
		right = 1
		hor +=1
	elif map_area[i][j+1] == "1":
		connections +=1	
		neighbors += 1
		right = 1
		hor +=1
	if map_area[i][j-1] == letter:
		answer = check_neighbors(i , j-1 )
		area += answer[0]
		vertices += answer[1]	
		neighbors += 1
		left = 1
		hor +=1
	elif map_area[i][j-1] == "1":
		connections +=1	
		neighbors += 1
		left = 1
		hor +=1
	
	if neighbors == 0:
		vertices += 4
	elif neighbors == 1:
		vertices += 2
	elif neighbors == 2:
		if hor == vert:
			if map_area[i+down-up][j+right-left] == letter or map_area[i+down-up][j+right-left] == "1":
				vertices += 1
			else:
				vertices += 2
		else:
			vertices += 0
				
	elif neighbors == 3:
		count = 0
		if down == 0:
			if map_area[i-1][j-1] != "1" and map_area[i-1][j-1] != letter:
				count +=1
			if map_area[i-1][j+1] != "1" and map_area[i-1][j+1] != letter:
				count +=1	
		elif up == 0:
			if map_area[i+1][j-1] != "1" and map_area[i+1][j-1] != letter:
				count +=1
			if map_area[i+1][j+1] != "1" and map_area[i+1][j+1] != letter:
				count +=1
		elif right == 0:
			if map_area[i-1][j-1] != "1" and map_area[i-1][j-1] != letter:
				count +=1
			if map_area[i+1][j-1] != "1" and map_area[i+1][j-1] != letter:
				count +=1
		elif left == 0:
			if map_area[i-1][j+1] != "1" and map_area[i-1][j+1] != letter:
				count +=1
			if map_area[i+1][j+1] != "1" and map_area[i+1][j+1] != letter:
				count +=1		
		vertices += count	
	
	elif neighbors == 4:
		count = 0	
		for l in [-1,1]:
			for k in [-1,1]:
				if map_area[i+k][j+l] != "1" and map_area[i+k][j+l] != letter:
					count+=1	
			
		vertices += count	
				
	return [area,vertices]			
		
	
def zerofy():
	for i in range(len(map_area)):
		for j in range(len(map_area[0])):
			if map_area[i][j] == "1":
				map_area[i][j] = "0"


with open('input12.txt') as fin:
	global map_area
	global regions_area
	global regions_vertices
	region_index = -1
	regions_area = []
	regions_vertices = []
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
				regions_vertices.append(answer[1])
				zerofy()
				
				
				
	sum = 0
	for index in range(len(regions_area)):
		sum += regions_area[index]*(regions_vertices[index])
		
	print(sum)
