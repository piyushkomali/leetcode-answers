class Solution:
    def isValid(self, s: str) -> bool:
        braces = {
            ")":"(",
            "}":"{",
            "]":"["
        }
        stack = []
        for char in s:
            if char in braces:
                if stack:
                    opening = stack.pop()
                else:
                    opening = "p"
                if braces[char] != opening:
                    return False
                
            else:
                stack.append(char)
        return not stack



