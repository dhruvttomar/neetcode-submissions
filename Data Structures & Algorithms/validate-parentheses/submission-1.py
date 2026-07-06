class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        m = {
            ')' : '(',
            '}' : '{',
            ']' : '['

        }
        for ch in s:
            if ch == '[' or ch == '(' or ch =='{':
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False

                top_bracket = stack.pop()

                if m[ch] == top_bracket:
                    continue
                else:
                    return False
        
        if len(stack) == 0:
            return True
        else:
            return False



            