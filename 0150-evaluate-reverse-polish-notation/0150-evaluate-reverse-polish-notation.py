class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        for current_token in tokens:
            if current_token not in "+-*/":
                stack.append(int(current_token))
                
            elif stack:
                current_num = stack.pop()
                
                if current_token == '+':
                    stack[-1] += current_num
                elif current_token == '-':
                    stack[-1] -= current_num
                elif current_token == '*':
                    stack[-1] *= current_num
                else:
                    stack[-1] = int(stack[-1]/current_num)
                    
        return stack[0]