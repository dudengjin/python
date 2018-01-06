count = 0
mSun = 0

while count < 100:
	if count %2 == 0:
		mSun = mSun - count
	else:
		mSun = mSun + count

	count += 1
print("和是%d"%mSun)
