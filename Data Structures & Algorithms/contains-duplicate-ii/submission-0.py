class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        i = 0
        j = 1
        while i != len(nums) - 1:  
            if j >= len(nums):
                i += 1
                j = i + 1
                continue
            if nums[i] == nums[j]:
                if abs(i-j) <= k:
                    return True
                else: 
                    i += 1
                    j = i + 1
            else: 
                j += 1
        return False