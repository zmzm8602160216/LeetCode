#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6


#Input: nums = [1]
#Output: 1


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    	for i in range(1,len(nums)):
    		nums[i]+=max(0,nums[i-1])
    	return max(nums)
