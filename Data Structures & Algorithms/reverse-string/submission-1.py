class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0 
        right = len(s)-1
        sub = ""
        while left < right:
            sub = s[left]
            s[left] = s[right]
            s[right] = sub
            left += 1
            right -= 1

