class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        logs_list = []
        letter_logs = []
        digit_logs = []
        
        for log in logs:
            words = log.split()
            
            if words[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append([' '.join(words[1:]), words[0]])
                
        letter_logs.sort()
        for letter_log in letter_logs:
            logs_list.append(' '.join(letter_log[::-1]))
        
        for digit_log in digit_logs:
            logs_list.append(digit_log)
        
        return logs_list
                