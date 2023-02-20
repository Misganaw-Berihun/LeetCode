class Solution:
    def isIPV4(self, ip):
        ipv4 =  ip.split('.')
        correct = True
        i = 0
        
        while correct and i < len(ipv4):
            j = 0
            
            while correct and j < len(ipv4):
                if not ipv4[i].isdigit():
                    correct = False
                j += 1
             
            correct_range = correct and (0 > int(ipv4[i]) or int(ipv4[i]) >= 256)
            empty = len(ipv4[i]) == 0
            leading = (not empty and ipv4[i][0] == '0' and len(ipv4[i]) != 1)
            if empty or correct_range or leading:
                correct = False
            i += 1
            
        return correct and i == 4
        
    def isIPV6(self, ip):
        ipv6 = ip.split(':')
        correct = True
        i = 0
        
        valid_chars = set(['a', 'b', 'c', 'd', 'e', 'f', 'A', 'B', 'C', 'D', 'E', 'F'])
        while correct and i < len(ipv6):
            if len(ipv6[i]) <=0 or len(ipv6[i]) > 4:
                correct = False
            
            else:
                for ch in ipv6[i]:
                    if not ch.isdigit() and ch not in valid_chars:
                        correct = False
            i += 1
            
        return correct and i == 8
            
            
    
    def validIPAddress(self, queryIP: str) -> str:
        ret = "Neither"
        if self.isIPV4(queryIP):
            ret = "IPv4"
        elif self.isIPV6(queryIP):
            ret = "IPv6"
        
        return ret
            