with open('input4.txt') as fin:
	line_list = []
	sum = 0
	for line in fin:
		line_list.append(line)
	line_list.append("."*len(line_list[-1]))	
	
	let = ["A","S","M"]	
	for i in range(len(line_list)):
		for j in range(len(line_list[i])):
			if line_list[i][j] == "A":
				cond1 = 1
				cond2 = 1
				cond3 = 1
				cond4 = 1
				for k in range(-1,2,2):
					if line_list[i-k][j-k] != let[k]:
						cond1 = 0		
					if line_list[i-k][j+k] != let[k]:
						cond2 = 0		
					if line_list[i+k][j-k] != let[k]:
						cond3 = 0	
					if line_list[i+k][j+k] != let[k]:
						cond4 = 0
				if cond1+cond2+cond3+cond4 == 2:
					sum +=1						
						 
					
	print(sum)
