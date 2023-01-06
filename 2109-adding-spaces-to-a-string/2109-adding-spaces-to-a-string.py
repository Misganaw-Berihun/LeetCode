class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        num_chars = len(s)
        num_spaces = len(spaces)
        modified_string = []
        
        pointer = 0
        
        for i in range(num_chars):
            if pointer < num_spaces and i == spaces[pointer]:
                modified_string.append(" ")
                pointer += 1
                
            modified_string.append(s[i])
            
        return ''.join(modified_string)