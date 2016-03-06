# for sorted array use two pointers
# O(n) runtime, O(1) space
class Solution:
	def twoSum(self, num, target):
		i, j = 0, len(num)-1
		while i < j:
			a, b = num[i], num[j]
			if a + b == target:
				return i + 1, j + 1
			elif a + b > target:
				j -= 1
			else:
				i += 1

num = [1, 3, 5, 6, 7]
target = 7
test = Solution()
print test.twoSum(num, target) #(1, 4)