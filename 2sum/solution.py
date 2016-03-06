def twoSum(num,target):
	#convert to hash
	dic = {}
	for i in range(len(num)):
		dic[num[i]] = i

	for elem in dic:
		res = target - elem
		if res in dic:
			return sorted([dic[elem]+1,dic[res]+1])

def twoSum1(num, target):
	#refactor
	dic = {}
	for index, n in enumerate(num, 1):
		rest = target - n
		if rest in dic:
			return dic[rest], index
		dic[n] = index

num = [5, 2, 7, 1, 9]
target = 3
print twoSum1(num, target)
