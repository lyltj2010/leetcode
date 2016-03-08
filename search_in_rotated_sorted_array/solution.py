# -*- coding: utf-8 -*-
"""
Suppose a sorted array is rotated at some pivot unknown to you beforehand.
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.
"""
class Solution(object):
	# time O(log n); space O(1)
	def foo(self,A,target):
		# binary search
		# determine the boundary 
		left, right = 0, len(A)
		while left != right:
			mid = (left + right) / 2
			if A[mid] == target:
				return mid
			if A[mid] >= A[left]: #left part
				if A[left] <= target and target < A[mid]:
					# A[left]..A[mid] is sorted
					right = mid
				else:
					left = mid + 1
			else:
				if A[mid] < target and target <= A[right-1]:
					# A[mid]..A[right] is sorted
					left = mid + 1
				else:
					right = mid
		return -1

A = [4,5,6,7,0,1,2]
s = Solution()
print s.foo(A, 1)