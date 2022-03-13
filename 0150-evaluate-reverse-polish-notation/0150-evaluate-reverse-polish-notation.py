class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        if len(tokens) == 1:
            return int(tokens[0])
        
        def do_ops(op1, op2, op):
            print(op1, op2, op)
            op1 = int(op1)
            op2 = int(op2)
            if op == "+":
                return op1 + op2
            elif op == "-":
                return op1 - op2
            elif op == "*":
                return op1 * op2
            else:
                return int(math.trunc(op1 / op2))
        
        tokens.reverse()
        stack = []
        
        while stack or tokens:
            curr = tokens.pop()
            if curr in ops:
                b = stack.pop()
                a = stack.pop()
                stack.append(do_ops(a, b, curr))            
            else:
                stack.append(curr)
                
            if len(tokens) == 0 and len(stack) == 1:
                return stack[0]
        
                  
        