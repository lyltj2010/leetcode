# -*- coding: utf-8 -*-
"""
You are climbing a stair case. 
It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?
"""
class Solution(object):
	# time O(n); space O(1)
	def climb_stairs(self,n):
		# iterate fibonacci
		# dp
		dp = [1 for i in range(n+1)]
		for i in range(2,n+1):
			dp[i] = dp[i-1] + dp[i-2]
		return dp[n]

n = 5
s = Solution()
print s.climb_stairs_1(n) #8
