class Solution:
    def find_bit(self, num1, num2):
        if (num1 & num2) > 0:
            return 1
        return 0
    
    def convert(self, num):
        minute, hr = 0, 0
        hr = (self.find_bit(num, 512) * 8 + self.find_bit(num, 256) * 4 + 
                self.find_bit(num, 128) * 2 + self.find_bit(num, 64))
        minute = (self.find_bit(num , 32) * 32 + self.find_bit(num , 16) * 16 + 
                  self.find_bit(num , 8) * 8 + self.find_bit(num , 4) * 4 + 
                  self.find_bit(num , 2) * 2 + self.find_bit(num , 1))
        
        minute_str = str(minute)
        if len(minute_str) < 2:
            minute_str = '0' * (2 - len(minute_str)) + minute_str
        
        if hr > 11 or minute >= 60:
            return ""
        return str(hr) +":" + minute_str
    
    def count_bits(self, num):
        cur = num
        cnt = 0
        
        while cur:
            cnt += (cur & 1)
            cur >>= 1
        
        return cnt
    
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []
        
        for i in range(768):
            if self.count_bits(i) == turnedOn:
                time = self.convert(i)
                if time != "":
                    ans.append(time)
                
        return ans
        