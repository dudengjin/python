#(1,2,3,4,5,6,7,8,10,age1=2,age3=155,age4=200)





def sum(a,b,c,*args,**kwargs):
	x = 0
	print(b)
	print(b)
	print(c)
	print(args)
	print(kwargs)
	x += a
	x += b
	x += c
	for i in args:
		x += i
	for k,v in kwargs.items():
		x += v

	return x		
		

result = sum(1,2,3,4,5,6,7,8,10,age1=2,age3=155,age4=200)
print(result)





