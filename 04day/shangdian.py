# 10家店 一个2包辣条 1包1元

money = 0
count = 1
while count  <= 10:
	mark = 1 # 一共买了几次
	while mark <= 2:
		money = money + 1
		mark += 1
		

	print("走了%d"%count)
	count += 1

print("一共花了%f元"%money)
