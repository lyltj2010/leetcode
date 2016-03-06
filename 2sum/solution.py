def twoSum(num,target):
	#convert to hash
	dic = {}
	for i in range(len(num)):
		dic[num[i]] = i

	for elem in dic:
		res = target - elem
		if res in dic:
			return sorted([dic[elem]+1,dic[res]+1])

num = [5, 2, 7, 1, 9]
target = 3
print twoSum(num, target)
