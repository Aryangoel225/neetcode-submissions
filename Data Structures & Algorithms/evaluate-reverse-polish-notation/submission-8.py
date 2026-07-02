class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            op = tokens[i]
            if op == "+" or op == "-" or op == "*" or op == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                if op == "+":
                    num = num1 + num2
                elif op == "-":
                    num = num2 - num1
                elif op == "*":
                    num = num2 * num1
                elif op == "/":
                    num = int(num2 / num1)
                stack.append(num)
            else:
                stack.append(int(op))
        return stack[0]
            
        