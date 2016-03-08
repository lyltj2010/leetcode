# -*- coding: utf-8 -*-
"""
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
For example, Given [100, 4, 200, 1, 3, 2], The longest consecutive elements sequence is [1,
2, 3, 4]. Return its length: 4.
Your algorithm should run in O(n) complexity
"""
class Solution(object):
	# time O(n); space O(n)
	def foo(self,A):
		# unsorted and O(n), hash is the way
		dic = {i: False for i in A} # not visited
		max_len = 1
		for i in dic:
			if dic[i] == False:
				left = i - 1; left_len = 0
				while left in dic:
					left_len += 1
					dic[left] = True
					left -= 1
				
				right = i + 1; right_len = 0
				while right in dic:
					right_len += 1
					dic[right] = True
					right += 1
				max_len = max(max_len,left_len + 1 + right_len)
		return max_len


A = [100, 4, 200, 1, 3, 2]
s = Solution()
print s.foo(A) # 4
