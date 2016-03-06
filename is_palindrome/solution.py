class Solution:
	def is_palindrome(self, string):
		# use two pointers
		i, j = 0, len(string)-1
		while i <= j:
			# skip non alpha char
			while not string[i].isalpha():
				i += 1
			while not string[j].isalpha():
				j -= 1

			a, b = string[i].lower(), string[j].lower()
			if  a != b:
				return False
			i += 1
			j -= 1
		return True

str1 = "A man, a plan, a canal: Panama"
test = Solution()
print test.is_palindrome(str1)