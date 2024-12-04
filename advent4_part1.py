with open('input4.txt') as fin:
	line_list = []
	sum = 0
	for line in fin:
		line_list.append(line)
	line_list.append("."*len(line_list[-1]))	
	
	let = ["X","M","A","S"]	
	for i in range(len(line_list)):
		for j in range(len(line_list[i])):
			if line_list[i][j] == "X":
				cond1 = 1
				cond2 = 1
				cond3 = 1
				cond4 = 1
				cond5 = 1
				cond6 = 1
				cond7 = 1
				cond8 = 1
				for k in range(1,4):
					try:
						if line_list[i][j-k] != let[k]:
							cond1 = 0
					except:
						cond1 = 0		
					try:
						if line_list[i][j+k] != let[k]:
							cond2 = 0
					except:
						cond2 = 0
					try:			
						if line_list[i-k][j] != let[k]:
							cond3 = 0
					except:
						cond3 = 0	
					try:	
						if line_list[i+k][j] != let[k]:
							cond4 = 0
					except:
						cond4 = 0
					try:		
						if line_list[i-k][j-k] != let[k]:
							cond5 = 0
					except:
						cond5 = 0
					try:	
						if line_list[i-k][j+k] != let[k]:
							cond6 = 0
					except:
						cond6 = 0	
					try:	
						if line_list[i+k][j+k] != let[k]:
							cond7 = 0
					except:
						cond7 = 0
					try:		
						if line_list[i+k][j-k] != let[k]:
							cond8 = 0
					except:
						cond8 = 0	
				sum += cond1 + cond2 + cond3+ cond4+ cond5+ cond6+ cond7+ cond8						
						 
					
	print(sum)
