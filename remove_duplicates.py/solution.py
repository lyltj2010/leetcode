# -*- coding: utf-8 -*-
"""
Given a sorted array, remove the duplicates in place such that each element appear only once
and return the new length.
Do not allocate extra space for another array, you must do this in place with constant memory.
For example, Given input array A = [1,1,2],
Your function should return length = 2, and A is now [1,2].
"""
class Solution(object):
	def remove_duplicates(self, alist):
		# @param sorrted array
		# @return integer length
		for i in range(len(alist)-2):
			if alist[i] == alist[i+1]:
				del alist[i+1]
		return len(alist)

A = [1,1,2,3,5,5]
s = Solution()
print s.remove_duplicates(A)