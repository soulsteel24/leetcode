class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        operand_stack =[]
        operator = ('+','-','/','*')
        for i in range(len(tokens)):
            if tokens[i] not in operator:
                num_stack.append(int(tokens[i]))
            else:
                x = num_stack.pop()
                y = num_stack.pop()
                if tokens[i] == '+':
                    num_stack.append(x + y)
                elif tokens[i] == '*':
                    num_stack.append(x*y)
                elif tokens[i] == '/':
                    num_stack.append(int(y/x))
                elif tokens[i] == '-':
                    num_stack.append(y-x)
        
        return num_stack[0]