# Given an array of integers, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

# You may assume that each input would have exactly one solution.

# Input: numbers={2, 7, 11, 15}, target=9
# Output: index1=1, index2=2

class Solution:
	# @return a tuple, (index1, index2)
	def twoSum(self, num, target):
		map = {}
		for x in xrange(0,len(num)):
			if num[x] not in map:
				map[target-num[x]] = x+1
			else:
				return map[num[x]],x+1
		return -1,-1

number = [2,7,11,15]
target = 18
test = Solution()
print test.twoSum(number, target)