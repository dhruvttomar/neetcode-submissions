class Solution:
    def reverseString(self, s: List[str]) -> None:
        b = 0
        p = 'a'
        e = -1
        stringlen = len(s)
        i = 0
        while i < (stringlen)/2:
            p = s[b]
            s[b] = s[e]
            s[e] = p
            b += 1
            e -= 1
            i += 1