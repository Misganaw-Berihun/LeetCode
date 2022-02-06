class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        exp = ""
        
        s = s.strip()
        for i,ch in enumerate(s):
            if ch == " ":
                continue
            
            if ch.isdigit():
                exp += ch
            
            if ch in ('+','-','*','/') or i == len(s) - 1:
                if stack and (stack[-1] == '*' or stack[-1] == '/'):
                    op = stack.pop()
                    num = stack.pop()
                    
                    if op == '*':
                        res = num * int(exp)
                    elif op == '/':
                        res = math.trunc(num / int(exp))
                    
                    stack.append(res)
                    

                else:
                    stack.append(int(exp))
                
                if i != len(s) - 1:
                    stack.append(ch)
                
                exp = ""
        
        stack = stack[::-1]
        while len(stack) >= 3:
            num1 = stack.pop()
            op  = stack.pop()
            num2 = stack.pop()
            
            if op == '+':
                stack.append(num1 + num2)
            elif op == '-':
                stack.append(num1 - num2)
                
        return stack.pop()
            
                
                    
        
                
                
            
        
    
        