def print_sum(a = 100,mode = 0):
	sum = 0
	if not mode:
		print("for")
		for i in range(1,a+1):
			sum += i
	else:
		print("while")
		count = 1
		while count <= a:
			sum += count
			count += 1
	
	return sum

result = print_sum(10,12)
print(result)
	
