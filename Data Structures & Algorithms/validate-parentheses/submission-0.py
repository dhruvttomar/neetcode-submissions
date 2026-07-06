class Solution:
    def isValid(self, s: str) -> bool:
        dic = {")": "(", "}": "{", "]": "["}
        val = []
        for char in s:
            if char not in dic:
                val.append(char)
            else:
                if len(val) > 0:
                    top_element = val.pop()
                else:
                    top_element = "#"
                if dic[char] != top_element:
                    return False                    
        return len(val) == 0