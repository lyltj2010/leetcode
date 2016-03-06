# use binary search for sorted array
def bsearch(alist, item):
	#return index of item in alist, none if not found
	left, right = 0, len(alist)-1
	while left <= right:
		mid = (left + right)/2
		if alist[mid] == item:
			return mid + 1 # not zero based this problem
		elif alist[mid] > item:
			right = mid -1
		else:
			left = mid + 1

def twoSum(num, target):
	for i in range(len(num)):
		rest = target - num[i]
		search = bsearch(num[i+1:], rest)
		if search == None:
			continue
		else:
			return i + 1, i + 1 + search

num = [1, 3, 5, 6, 7]
target = 7
print twoSum(num, target) #(1, 4)
