with open('input1.txt') as fin:
	sum = 0
	list1 = []
	list2 = []
	for line in fin:
		nums = line.strip("\n").split("   ")
		num1 = nums[0]
		num2 = nums[1]
		list1.append(int(num1))
		list2.append(int(num2))
	
	list1.sort()
	list2.sort()
	
	for j in range(len(list1)):
		sum += abs(list2[j] - list1[j])
	print(sum)	
			
