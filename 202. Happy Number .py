#Input: n = 19
#Output: true
#Explanation:
#12 + 92 = 82
#82 + 22 = 68
#62 + 82 = 100
#12 + 02 + 02 = 1

class Solution:
    def isHappy(self, n: int) -> bool:

    	seen=set()

    	while n not in seen:
    		seen.add(n)
    		n = sum([int(x)**2 for x in str(n)])

    	return n==1
