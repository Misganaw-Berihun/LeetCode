class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        top = popped[0]
        i = 0
        j = 1
        
        while i != len(pushed) and pushed[i] != top:
            stack.append(pushed[i])
            i += 1
        
        i += 1
        while i < len(pushed):
            if not stack:
                stack.append(pushed[i])
                i += 1
            elif stack[-1] != popped[j]:
                if popped[j] == pushed[i]:
                    i += 1
                    j += 1
                else:
                    stack.append(pushed[i])
                    i += 1
            else:
                stack.pop()
                j += 1
            
        while stack:
            if stack.pop() != popped[j]:
                return False
            else:
                j += 1
                
        return not stack
        