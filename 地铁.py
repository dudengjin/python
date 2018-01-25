list = []     # 用来记录每个月的地铁费用
allcount = 0  # 用来记录一共乘坐多少次地铁


# 计算每个月的费用
def sub_money(distance,count,month):
	info = {}
	money = 0
	sum = 0	# 每个月的地铁费用
	global allcount  #  声明要修改全局变量
	allcount += count * 30
	for i in range(0,count*30):
		if ditance <= 6:
			money = 3
		elif 6 < ditance  and ditance <= 12:
			money = 4
		elif 12 < ditance  and ditance <= 22:
			money = 5
		elif 22 < ditance and ditance <= 32:
			money = 6
		elif ditance > 32:
			if (ditance-32)%20 == 0:
				money = 6 + (ditance-32)/20
			else:
				money = 6 +int((ditance-32)/20)+1
		if sum >= 100 and sum >= 150:
				money = money * 0.8
		elif sum >= 150 and sum >= 400:
				money = money * 0.5
		sum += money
	
	# 用一个字典装月份和这个月份的钱  todo输入重复月份会覆盖
	info[month] = sum
	list.append(info)

	

# 计算总钱
def sum_money():
	sum = 0
	for i in list:
		for k,v in i.tiems():
			print("%d月份花了%0.2f元"%(k,v))
			sum += v
	return sum


# 用户菜单输入
def user_input():
	loop = True
	while loop:
		mode = int(input("菜单 1.乘坐 2.计算\n"))
		if mode == 1:
			distance = float(input("请输入距离"))
			month = int(input("请输入月份"))
			count = int(input("请输入每天乘坐的次数"))
			if month >= 13 or month < 1:
				print("输入的不合法")
			elif count <= 0:
				print("输入的不合法")
			else:
				sub_money(distance,count,month)
		else:
			result = sun_money()
			print("总共花了%0.2f元,一共坐了%d次地铁"%(result,allcount))
			loop = False

user_input()






