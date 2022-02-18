class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        
        for i,ch in enumerate(s):
            if ch.isdigit():
                temp = "" 
                if stack and stack[-1].isdigit() and s[i-1] != '[':
                    stack.append(stack.pop() + ch)
                else:
                    stack.append(ch)
            elif ch.isalpha():
                if stack and stack[-1].isalpha():
                    stack.append(stack.pop() + ch)
                else:
                    stack.append(ch)
            elif ch == ']':
                if len(stack) >= 2:
                    temp = stack.pop() * int(stack.pop())
                    stack.append(temp)
                    
                temp = ""
                while stack and stack[-1].isalpha():
                    temp = stack.pop() + temp
                    
                stack.append(temp)
        
        ans = stack.pop()
        if stack:
            ans = ans * int(stack.pop())
    
        return ans
                    
         
                    
        
                    
        
                
            
                
            
                