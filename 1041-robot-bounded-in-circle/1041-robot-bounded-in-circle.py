class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y = 0, 0
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        index = 0
        for _ in range(4):
            for inst in instructions:
                if inst == 'G':
                    x += directions[index][0]
                    y += directions[index][1]
                elif inst == 'R':
                    index = (index + 1) % 4
                else:
                    index = (index - 1) % 4
        
        return x == 0 and y == 0
    