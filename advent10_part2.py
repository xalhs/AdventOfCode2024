def check_around(i,j,height , vals , map_area):
	total = 0
	height = int(height)
	try:
		if int(map_area[i-1][j]) == height+1:
			total+= vals[(i-1,j)]
	except:
		pass		
	try:		
		if int(map_area[i+1][j]) == height+1:
			total+= vals[(i+1,j)]
	except:
		pass	
	try:	
		if int(map_area[i][j-1]) == height+1:
			total+= vals[(i,j-1)]
	except:
		pass	
	try:
		if int(map_area[i][j+1]) == height+1:
			total+= vals[(i,j+1)]
	except:
		pass	
	
	return total	
		


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
						vals[(i,j)] = 1
				else:		
					if height == str(k):
						score = check_around(i,j,height , vals , map_area)
						vals[(i,j)] = score
						if k == 0:
							sum+=score
	print(sum)						
							
				
				
			
