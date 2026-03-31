class Solution:
    def isValid(self, s: str) -> bool:
        closing = {")":"(","]":"[","}":"{"}
        stack = []

        for c in s:
            if c in closing and stack:
                opening = stack.pop()
                if opening != closing[c]:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
