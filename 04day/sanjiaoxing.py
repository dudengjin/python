count = 0 
while count <=5:

	kongge = 0
	while kongge < 5 - count:
		print(end=" ")
		kongge += 1

	star = 0
	while star < count: 
		print("*",end=" ")
		star += 1

	print("")
	count += 1
