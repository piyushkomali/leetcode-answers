class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces = {")":"(", "}":"{", "]":"["}

        for character in s:
            if character not in braces:
                stack.append(character)

            elif not stack:
                return False
            elif stack.pop() != braces[character]:
                return False
        return len(stack) == 0
        