# -*- coding: utf-8 -*-
"""
Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""
class Solution(object):
	def remove_duplicates(self, A):
		# @param sorrted array
		# @return integer
		if len(A) == 0:
			return 0
		j = 0 # use a pointer
		for i in range(len(A)):
			if A[i] != A[j]:
				# move non duplicated elem to left part
				A[i], A[j+1] = A[j+1], A[i]
				j += 1
		return j + 1

alist = [1,1,1,2,3,5,5]
s = Solution()
print s.remove_duplicates(alist) #