class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbs = {}
        for i in range(len(nums)):
            if (target - nums[i]) in numbs:
                return [numbs[target - nums[i]], i]
            else: 
                numbs[nums[i]] = i 
        return [0,0]
