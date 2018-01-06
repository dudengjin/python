evenNumber = 0 # 这是要求的偶数和
oddNumber = 0 # 这是要求的奇数和
allSum = 0
x = 0
while x < 100:
	print("当前数字:%d"%x)
	x += 1
	if x%2 == 0: #这是偶数
		evenNumber = evenNumber + x
	elif x%2 != 0:
		oddNumber = oddNumber + x

	
print("偶数和为:%d"%evenNumber)
print("奇数和为:%d"%oddNumber)
print("和为:%d"%(evenNumber+oddNumber))
