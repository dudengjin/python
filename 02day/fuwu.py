# 这是服务器的帐号和密码
account = 123456
pwd = "abc"

#这是你输入的帐号和密码
myAccount = int(input("请输入帐号:\n"))
myPwd =input("请输入密码\n")

if myAccount == account and myPwd == pwd:
	print("登录成功")
elif myAccount != account:
	print("帐号错误")
elif myPwd != pwd:
	print("密码错误")
else:
	print("系统泡妞去啦")
