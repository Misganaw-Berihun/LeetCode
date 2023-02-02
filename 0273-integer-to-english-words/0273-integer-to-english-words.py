class Solution:
    def readUpToThousand(self, num):
        words  = [
                    ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"],
                    ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"],
                    ["Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"],
                    ["Hundred"]
                 ]
        
        num_inwords = []
        last_two = num  % 100
        hundreds = num // 100
        
        if 10 <= last_two < 20:
            num_inwords.append(words[1][last_two % 10])
            
        else:
            tens = last_two // 10
            ones = last_two % 10
            if ones != 0:
                num_inwords.append(words[0][ones])
                
            if tens != 0:
                num_inwords.append(words[2][tens - 2])
            
        
        if hundreds != 0:
            num_inwords.append(words[3][0])
            num_inwords.append(words[0][hundreds])
        
        return ' '.join(num_inwords[::-1])
        
            
        
    def numberToWords(self, num: int) -> str:
        words = [ "Thousand", "Million", "Billion"]
        
        if num == 0:
            return "Zero"
        
        ans = []
        ptr = 0
        while num > 0:
            temp = num % 1000
            t = (num // 1000) % 1000
            read = self.readUpToThousand(temp)
            if read:
                ans.append(read)
            
            if t > 0:
                ans.append(words[ptr])
            num = num // 1000
            ptr += 1
        
    
        return ' '.join(ans[::-1])
            
    
        