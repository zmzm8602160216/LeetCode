##Input: nums = [2,7,11,15], target = 9
##Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) ->List[int]:
    	dict={}

    	for idx,ele in enumerate(nums):
    		if target-ele in dict:
    			return[dict[target-ele],idx]
    		dict[ele]=idx