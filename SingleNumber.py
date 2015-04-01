# Given an array of integers, every element appears twice except for one. Find that single one.

# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
    	result = 0
    	for x in xrange(0,len(A)):
    		result = result ^ A[x]
    	return result

testClass = Solution()
testArray = [1,1,2,2,3,7,3]
result = testClass.singleNumber(testArray)

print testArray
print result