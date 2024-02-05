class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            #print(stack)
            if token == "*":
                stack.append(stack.pop()*stack.pop())
            elif token == "/":
                decimal = stack.pop()
                stack.append(int(stack.pop()/decimal))
            elif token == "+":
                stack.append(stack.pop()+stack.pop())
            elif token == "-":
                minus = stack.pop()
                stack.append(stack.pop()-minus)
            else:
                stack.append(int(token))
        return stack[-1]