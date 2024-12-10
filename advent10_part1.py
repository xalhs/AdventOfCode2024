def check_around(i,j,height , vals , map_area):
	
	height = int(height)
	try:
		if int(map_area[i-1][j]) == height+1:
			vals[(i,j)] = vals[(i,j)] + [x for x in vals[(i-1,j)] if x not in  vals[(i,j)] ]
	except:
		pass		
	try:		
		if int(map_area[i+1][j]) == height+1:
			vals[(i,j)] = vals[(i,j)] + [x for x in vals[(i+1,j)] if x not in  vals[(i,j)] ]
	except:
		pass	
	try:	
		if int(map_area[i][j-1]) == height+1:
			vals[(i,j)] = vals[(i,j)] + [x for x in vals[(i,j-1)] if x not in  vals[(i,j)] ]
	except:
		pass	
	try:
		if int(map_area[i][j+1]) == height+1:
			vals[(i,j)] = vals[(i,j)] + [x for x in vals[(i,j+1)] if x not in  vals[(i,j)] ]
	except:
		pass	
	
	return vals	
		


with open('input10.txt') as fin:
	map_area = []
	for line in fin:
		map_area.append(line.rstrip("\n")+".")
	
	map_area.append("."*len(map_area[-1]))
	vals = {}
	sum = 0
	for k in reversed(range(10)):	
		for i,row in enumerate(map_area):
			for j,height in enumerate(row):
				if k == 9:
					if height == str(k):
						vals[(i,j)] = [[i,j]]
				else:		
					if height == str(k):
						vals[(i,j)] = []
						vals = check_around(i,j,height , vals , map_area)
						if k == 0:
							sum+=len(vals[(i,j)])
	print(sum)						
							
				
				
					
					
				
				
					
