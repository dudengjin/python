account = "yiwangxi" 
pwd = 123456

vbook = ["水浒传","圣经","物种起源","红楼梦","老人与海","小王子","昆虫记","茶花女","复活","老舍","活着","假如给我三天光明"]


print("欢迎进入北京图书管理系统".center(30,"*"))


# 管理员登录系统
def pass_Word():
	myAccount = input("请输入管理员帐号")
	myPwd = int(input("请输入管理员密码"))

	if account == myAccount and pwd == myPwd:
		print("登录成功")
	elif account != myAccount and pwd != myPwd:
		print("密码或账户输入错误")




def reader():
	list = []
	dic = {}
	name = "dudengjin"
	libraryCard = "04551"
	myName = input("请输入您的姓名")
	myLibraryCard =input("请输入您的图书证号")
	
	if libraryCard == myLibraryCard and name == myName:
		print("欢迎进入图书系统")
	else:
		print("您输入的信息有误")
	dic["name"] = name
	dic["libraryCard"] = libraryCard
	list.append(dic)
	print(list)
 
	


def borrow():
	print('现在的书有:')
	print(vbook)
	myBook = input('请输入书名:')
	day = int(input("请输入要借的时长"))
	if day <= 30:
		print("在借书范围内,可借出")
	elif day >= 30:
		print("超出范围，请重新输入")
	for i in vbook:
		print(i)
		if myBook == i:
			a = vbook.index(i)
			vbook.pop(a)
			print("借书成功，你要借的书是%s"%a)
	



def danaged():
	mybook = input('请输入你要还的书名:')
	day = int(input("借的时长"))
	if day <= 30:
		vbook.append(mybook)
		print("还书成功")
	elif day > 30:
		buckle = (day-30)*2
		vbook.append(mybook)
		print("超出预计还书时间,扣款%.2f元"%buckle)





def show_op():
	while True:
		mode = int(input("请输入功能信息: 0、登录系统 1、读者信息 2、借书信息 3、还书信息 4、退出"))
		if mode == 0:
			pass_Word()
		elif mode == 1:
			reader()
		elif mode == 2:
			borrow()	
		elif mode == 3:
			danaged()
		elif mode == 4:
			break


show_op()
