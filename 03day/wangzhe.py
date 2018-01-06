account = "yiwangxi"
pwd = "123456"

isLoop = True
count = 0

while isLoop:
	myAccount = input("请输入帐号")
	myPwd = input("请输入密码")


	if myAccount == account and myPwd == pwd:
			print("登录成功")
			lcoation =int(input("请选择英雄 0ADC 1肉 3法师"))
			if lcoation == 0:
				print("鲁班大师")
			elif lcoation == 1:
				print("程咬金")
			elif lcoation == 3:
				print("王昭君")
		
			isLoop = False
		
	else:
			print("登录失败,请重新登录")
			count+= 1
			if count == 3:
				isLoop = False
				print("次数过多,请注意.")
