with open('input2.txt') as fin:
	sum = 0
	for line in fin:
		list1 = [int(x) for x in line.strip("\n").split(" ")]
		safe = False
		for j in range(len(list1)):
			inc = False
			dec = False	
			for i,num in enumerate(list1):
				if i == j:
					continue
				if i ==0 or (j==0 and i==1):
					prev_num = num
					continue
				else:	
					if num == prev_num:
						inc = False
						dec = False
						break
					elif num>prev_num:
						if dec == True:
							dec = False
							break
						else:
							if num -prev_num >=1 and num - prev_num <=3:
								inc = True
							else:
								inc = False
								break	
					elif num < prev_num:
						if inc == True:
							inc = False
							break
						else:
							if prev_num - num >=1 and prev_num-num <=3:
								dec = True
							else:
								dec = False
								break		
					prev_num = num			
												
			if dec or inc:
				safe = True	
		if safe == True:
			sum+=1		
	
	print(sum)	
			
