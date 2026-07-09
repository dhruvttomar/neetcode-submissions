class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        left = 0
        mx = 0

        for right in range(len(s)):
            current = s[right] 
            if current in mp and mp[current] >= left:
                left = mp[current] + 1
            mp[current] = right
            mx = max(mx, right - left + 1)
        return mx
        