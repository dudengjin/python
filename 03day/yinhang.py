# 去银行取钱

account = "123456"
pwd = 123456
money = 5210


myAccount = input("请输入帐号")
myPwd = int(input("请输入密码"))

if myAccount == account  and myPwd == pwd:
	print("登录成功")
	
	mode = int(input("请选择方式  a 取 b 存")) 
	if mode == "a":

		moneyCount = int(input("请输入金额"))
		
		if money > moneyCount:
			print("你取了%d元 还剩%d元"%(moneyCount,money-moneyCount))
		else:
			print("余额不足")

	elif mode == "b":
		if money >= moneyCount:
			print("你存了%d元 余额为%d元"%(moneyCount,money+moneyCount))

else:
	print("非法账户")


"""
# 石头剪刀布

石头 = 1
剪刀 = 2
布 = 3

import random
while True:
	computer = random.randint(1,3)
	own = int(input("请输入1,2,3"))

	
	if own == 1 and computer == 2:
		print("我赢")
	elif own == 2 and computer == 3:
		print("我赢")
	elif own == 3 and computer == 1:
		print("我赢")
	elif own == computer:
		print("平局")

	else:
		print("电脑赢")

# 石头剪刀布

石头 = 1
剪刀 = 2
布 = 3

import random
computer = random.randint(1,3)
own = int(input("请输入1 石头 ,2 剪刀,3 布"))

if own <= 3 and own > 0:
	if (own == 1 and computer== 2) or (own == 2 and computer == 3) or (own == 3 and computer == 1):
		print("我赢")
	elif own == computer:
		print("平局")

	else:
		print("你输了")

else:
	print("输入不合法")
"""
