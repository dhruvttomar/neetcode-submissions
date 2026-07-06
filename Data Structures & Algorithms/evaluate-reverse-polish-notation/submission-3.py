class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        calc = 0
        for i in tokens:
            if i == '+':
                calc = nums[-1] + nums[-2]
                nums.pop()
                nums.pop()
                nums.append(calc)
            elif i == '-':
                calc = nums[-2] - nums[-1]
                nums.pop()
                nums.pop()
                nums.append(calc)
            elif i == '*':
                calc = nums[-2] * nums[-1]
                nums.pop()
                nums.pop()
                nums.append(calc)
            elif i == '/':
                calc = int(nums[-2] / nums[-1])
                nums.pop()
                nums.pop()
                nums.append(calc)
            else: 
                nums.append(int(i))
        return nums[0]
