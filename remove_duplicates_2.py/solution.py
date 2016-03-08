# -*- coding: utf-8 -*-
"""
Follow up for ”Remove Duplicates”: What if duplicates are allowed at most twice?
For example, Given sorted array A = [1,1,1,2,2,3],
Your function should return length = 5, and A is now [1,1,2,2,3]
"""
class Solution(object):
	def remove_duplicates_2(self,A):
		# start from A[2]
		# use a pointer
		if len(A) <= 2:
			return len(A)
		j = 2 # the pointer
		for i in xrange(2,len(A)):
			if A[i] != A[j-2]:
				A[j] = A[i]
				j += 1
		return j

A = [1,1,1,2,2,3]
s = Solution()
print s.remove_duplicates_2(A) # 5