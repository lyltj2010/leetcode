# -*- coding: utf-8 -*-
"""
You are climbing a stair case. 
It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
class Solution(object):
	def climb_stairs(self,n):
		# use recursive
		if n in [1, 2]:
			return 1
		steps = self.climb_stairs(n-1) + self.climb_stairs(n-2)
		return steps

n = 5
s = Solution()
print s.climb_stairs(n) #5
