
class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            string = []
            for i in s:
                
                if i == '0':
                    string.append('1')
                else:
                    string.append('0')
            return ''.join(string[::-1])
        
        def help(s,a,k):
            if a == n:
                return s[k - 1]
            a += 1
            temp = s
            s = s + "1" 
            temp2 = invert(temp)
            s +=  temp2
            su = help(s,a,k)
            return su



        return help("0", 1, k)