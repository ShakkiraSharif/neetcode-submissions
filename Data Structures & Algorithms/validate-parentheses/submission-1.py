class Solution:
    def isValid(self, s: str) -> bool:
        dic={
            ']':'[',
            ')':'(',
            '}':'{'
        }
        stack=[]
        for c in s:
            if c in "({[":
                stack.append(c)
            elif not stack or stack[-1]!=dic[c] :
                return False
            else:
                stack.pop()
        return len(stack)==0
        