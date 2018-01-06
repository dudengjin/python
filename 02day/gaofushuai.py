height = float(input("请输入你的身高"))
shenjian = float(input("请输入你的身价"))
yanzhi = int(input("请输入你的颜值分"))

if height > 180 and shenjian > 1000000 and yanzhi > 90:
	print("是高富帅")

elif height < 180 and shenjian > 1000000 and yanzhi > 90:
	print("是富帅")

elif height < 180 and shenjian < 1000000 and yanzhi > 90:
	print("是帅")

elif height < 160 and shenjian < 100 and yanzhi < 60:
	print("是矮穷矬")

else:
	print("你是平民")
