# 算一下平年还是闰年

year = int(input("请输入一个年份"))

if year > 0:
	if year %4 == 0 and year %100 != 0:
		print("这个是闰年")
	elif year %400 == 0:
		print("这个是闰年")
	else:
		print("这个是平年")

else:
    print("你输入的年份不合法")




# 算一下平年还是闰年

year = int(input("请输入一个年份"))

if year > 0:

	if (year %4 == 0 and year %100 != 0) or year %400 == 0:
		print("这个是闰年")
	else:
		print("这个是平年")

else:
	print("你输入的年份不合法")
