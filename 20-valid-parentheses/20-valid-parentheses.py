class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        look = { ")" : "(" , "]" : "[" , "}" : "{" }
        for p in s:
            if p in look.values():
                stack.append(p)
            elif stack and look[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
