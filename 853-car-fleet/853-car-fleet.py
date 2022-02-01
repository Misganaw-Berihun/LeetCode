class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pos_speed = list(zip(position,speed))
        pos_speed.sort();
        
        for pos,sp in pos_speed:
            time = (target - pos) / sp
                        
            while stack and stack[-1] <= time:
                stack.pop()
            
            stack.append(time)
                        
        return len(stack)
                
                
        
        
        