class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Every open parentheses we add to stack corresponding end
        # On ending bracket, pop stakc and see if match.

        pair = {"]":"[","}":"{",")":"("}

        for c in s:
            if c in pair:
                if stack and stack[-1] == pair[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
            
            