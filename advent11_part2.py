
global memory
global recursion_skip
memory = {}
recursion_skip = 5

def basics(num , n):
	if (num,n) in memory:
		return memory[(num,n)]
	if n==0:
		return 1
	if num ==0:
		num = 1
		memory[(num , n-1)] = basics(num , n-1)
		return memory[(num , n-1)]
	elif num ==1:
		memory[(2 , n-3)] = basics(2 , n-3)
		memory[(0,n-3)] = basics(0,n-3)
		memory[(4,n-3)] = basics(4,n-3)
		
		return 2*memory[(2 , n-3)] + memory[(0,n-3)]  + memory[(4,n-3)] 	
	elif num == 2:
		memory[(4,n-3)] = basics(4,n-3)
		memory[(0,n-3)] = basics(0,n-3)
		memory[(8,n-3)] = basics(8,n-3)
		return 2*memory[(4,n-3)] + memory[(0,n-3)] + memory[(8,n-3)]
	elif num == 3:
		memory[(6,n-3)] = basics(6,n-3)
		memory[(0,n-3)] = basics(0,n-3)
		memory[(7,n-3)] = basics(7,n-3)
		memory[(2,n-3)] = basics(2,n-3)
		return memory[(6,n-3)] + memory[(0,n-3)] + memory[(7,n-3)] + memory[(2,n-3)] 
	elif num == 4:
		memory[(8,n-3)] = basics(8,n-3)
		memory[(0,n-3)] = basics(0,n-3)
		memory[(9,n-3)] = basics(9,n-3)
		memory[(6,n-3)] = basics(6,n-3)
		return memory[(8,n-3)] + memory[(0,n-3)] + memory[(9,n-3)] + memory[(6,n-3)]
	elif num == 5:
		total = 0
		memory[(2,n-5)] = basics(2,n-5)
		memory[(0,n-5)] = basics(0,n-5)
		memory[(4,n-5)] = basics(4,n-5)
		memory[(8,n-5)] = basics(8,n-5)
		total += 3*memory[(8,n-5)] + 2*memory[(0,n-5)] + 2*memory[(2,n-5)] + memory[(4,n-5)]
		return total
	elif num == 6:
		total = 0
		memory[(2,n-5)] = basics(2,n-5)
		memory[(5,n-5)] = basics(5,n-5)
		memory[(4,n-5)] = basics(4,n-5)
		memory[(7,n-5)] = basics(7,n-5)
		total += memory[(2,n-5)] + 2*memory[(4,n-5)] + 2*memory[(5,n-5)] + memory[(7,n-5)]
		memory[(9,n-5)] = basics(9,n-5)
		memory[(6,n-5)] = basics(6,n-5)
		total += memory[(9,n-5)] + memory[(6,n-5)]
		return total		
			
	elif num == 7:
		total = 0
		memory[(2,n-5)] = basics(2,n-5)
		memory[(8,n-5)] = basics(8,n-5)
		memory[(0,n-5)] = basics(0,n-5)
		memory[(7,n-5)] = basics(7,n-5)
		total += 2*memory[(2,n-5)] + memory[(8,n-5)] + memory[(0,n-5)] + memory[(7,n-5)]
		memory[(3,n-5)] = basics(3,n-5)
		memory[(6,n-5)] = basics(6,n-5)
		total += 2*memory[(6,n-5)] + memory[(3,n-5)]
		return total
	elif num == 8:
		total = 0
		memory[(2,n-5)] = basics(2,n-5)
		memory[(8,n-4)] = basics(8,n-4)
		memory[(7,n-5)] = basics(7,n-5)
		total += 2*memory[(2,n-5)] + memory[(8,n-4)]  + 2*memory[(7,n-5)]
		memory[(3,n-5)] = basics(3,n-5)
		memory[(6,n-5)] = basics(6,n-5)
		total += memory[(6,n-5)] + memory[(3,n-5)]
		return total
	elif num == 9:
		total = 0
		memory[(9,n-5)] = basics(9,n-5)
		memory[(8,n-5)] = basics(8,n-5)
		memory[(1,n-5)] = basics(1,n-5)
		memory[(4,n-5)] = basics(4,n-5)
		total += memory[(9,n-5)] + 2*memory[(8,n-5)] + memory[(1,n-5)] + memory[(4,n-5)]
		memory[(3,n-5)] = basics(3,n-5)
		memory[(6,n-5)] = basics(6,n-5)
		total += 2*memory[(6,n-5)] + memory[(3,n-5)]
		return total		
							
			
def nested_func(stones,n):
	tot = 0
	if n==0:
		return(tot + len(stones))

	for stone in stones:
		if len(str(stone)) ==1:
			tot += basics(stone, n)
		elif len(str(stone)) ==3:
			if n<=recursion_skip:
				tot+= len(memory[(stone , n)]) 
			else:	
				tot+= nested_func(memory[(stone,recursion_skip)] , n-recursion_skip)
				
		elif len(str(stone)) %2 ==0:
			temp1 = int(str(stone)[:int(len(str(stone))/2)])
			temp2 = int(str(stone)[int(len(str(stone))/2):])	
			tot+= nested_func([temp1,temp2] , n-1)
		else:
			tot+= nested_func([stone*2024] , n-1)
		
	return tot
					
	


import copy

with open('input11.txt') as fin:
	sum = 0
	for line in fin:
		stones = line.rstrip("\n").split(" ")
	stones = [int(x) for x in stones]	
	

	for k in range(10):
		basic_stone = [k]
		for i in range(5):
			j = 0
			while j < len(basic_stone):
				if basic_stone[j] ==0:
					basic_stone[j] = 1
				elif len(str(basic_stone[j])) %2 ==0:
					temp1 = int(str(basic_stone[j])[:int(len(str(basic_stone[j]))/2)])
					temp2 = int(str(basic_stone[j])[int(len(str(basic_stone[j]))/2):])	
					basic_stone[j] = temp1
					basic_stone.insert(j+1 , temp2)
					j +=1
				else:
					basic_stone[j] *= 2024
				j +=1	
				memory[(k,i+1)] = len(basic_stone)	
					
	for k in range(100,1000):
		basic_stone = [k]
		for i in range(recursion_skip+1):
			j = 0
			while j < len(basic_stone):
				if basic_stone[j] ==0:
					basic_stone[j] = 1
				elif len(str(basic_stone[j])) %2 ==0:
					temp1 = int(str(basic_stone[j])[:int(len(str(basic_stone[j]))/2)])
					temp2 = int(str(basic_stone[j])[int(len(str(basic_stone[j]))/2):])	
					basic_stone[j] = temp1
					basic_stone.insert(j+1 , temp2)
					j +=1
				else:
					basic_stone[j] *= 2024	
				j+=1		
			memory[(k,i+1)] = copy.copy(basic_stone)
						
	iterations = 75
	sum = nested_func(stones , iterations)
	print(sum)
