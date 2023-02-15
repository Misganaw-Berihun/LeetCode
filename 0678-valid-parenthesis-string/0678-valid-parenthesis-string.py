class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        
        stack = []
        indices = []
        for i in range(n):
            if s[i] == ')' and stack and s[stack[-1]] == '(':
                stack.pop()
            
            elif s[i] == '*':
                indices.append(i)
            
            else:
                stack.append(i)
            
        used = set()
        for i in range(len(stack)):
            found = False
            j = 0
            
            char = s[stack[i]]
            while not found and j < len(indices):
                if j in used:
                    j += 1
                    continue
                  
                if char == '(' and indices[j] > stack[i]:
                    found = True
                    used.add(j)
                
                elif char == ')' and indices[j] < stack[i]:
                    found = True
                    used.add(j)
                    
                j += 1
                
            if not found:
                return False
            
        return True
                
        