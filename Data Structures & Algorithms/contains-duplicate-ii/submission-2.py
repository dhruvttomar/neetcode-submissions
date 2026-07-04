class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        leftptr = 0
        for rightptr in range(len(nums)):
            if rightptr - leftptr > k:
                window.remove(nums[leftptr])
                leftptr += 1
            if nums[rightptr] in window:
                return True
            window.add(nums[rightptr])
        return False
            
