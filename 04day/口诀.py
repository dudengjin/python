count = 1
while count <= 9:
	
	row = 1

	while row <= count:
		print("%d*%d=%d"%(row,count,row*count),end="\t")
		row += 1
	print("")
	count += 1
