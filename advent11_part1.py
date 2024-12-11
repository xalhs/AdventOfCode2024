with open('input11.txt') as fin:
	for line in fin:
		stones = line.rstrip("\n").split(" ")
	stones = [int(x) for x in stones]	
	

	for i in range(25):
		j = 0
		while j < len(stones):
			if stones[j] ==0:
				stones[j] = 1
			elif len(str(stones[j])) %2 ==0:
				temp1 = int(str(stones[j])[:int(len(str(stones[j]))/2)])
				temp2 = int(str(stones[j])[int(len(str(stones[j]))/2):])	
				stones[j] = temp1
				stones.insert(j+1 , temp2)
				j +=1
			else:
				stones[j] *= 2024	
			j+=1	
	
	print(len(stones))
