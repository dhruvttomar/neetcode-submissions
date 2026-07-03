class Solution:
    def validPalindrome(self, s: str) -> bool:
        begin, end = 0, len(s)-1
        while begin < end: 
            if s[begin] != s[end]:
                leftstr, rightstr = s[begin + 1:end+ 1], s[begin: end]
                return (leftstr == leftstr[::-1]) or (rightstr == rightstr[::-1]) 
            begin, end = begin + 1, end - 1
        return True
        