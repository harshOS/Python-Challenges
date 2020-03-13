# problem link - https://edabit.com/challenge/hFNhDGNt8CNjSNnG9
def setify(lst):
	res =[]
	for i in lst:
		if i not in res:
			res.append(i)
	return res
print(setify([1, 3, 3, 5, 5]))