class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in range(len(s)):
            if self.isvalid(s[i]):
                arr.append(s[i].lower())
        return arr == arr[::-1]
    def isvalid(self, x):
        return  (ord('A') <= ord(x) <= ord('Z') or ord('a') <= ord(x) <= ord('z') or ord('0') <= ord(x) <= ord('9')) 

