class Solution:
    def isValid(self, s: str) -> bool:
        closeDict = {"{":"}","(":")","[":"]"}
        stack = []
        for char in s:
            if char in closeDict:
                stack.append(closeDict[char])
            elif stack:
                latest = stack.pop()
                if latest != char:
                    return False
            else:
                return False

        return len(stack) == 0 