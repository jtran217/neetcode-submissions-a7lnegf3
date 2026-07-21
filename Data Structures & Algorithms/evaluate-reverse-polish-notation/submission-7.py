class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operation = "+-*/"

        for token in tokens:
            if token in operation:
                val1 = int(stack.pop())
                val2 = int(stack.pop())
                val3 = 0
                if token == "+":
                    val3 = val1 + val2
                elif token == "-":
                    val3 = val2 - val1
                elif token == "*":
                    val3 = val1 * val2
                else:
                    val3 = int(float(val2)/val1)
                stack.append(val3)
            else:
                stack.append(token)
        
        return int(stack.pop())
