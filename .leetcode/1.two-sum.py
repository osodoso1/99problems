#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}#making value:index dict
        for i, n in enumerate(nums):
            diff = target - n 
            if diff in prevMap:
                return [prevMap[diff],i]
            prevMap[n] = i
        return
    #making a previous map to hold index of values and returning values that would equal 4
# @lc code=end

