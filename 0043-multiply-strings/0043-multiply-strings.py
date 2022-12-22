class Solution:
    def mul(self,num, digit, zeros):
        size = len(num)
        res = []
        carry = 0
        for i in range(size - 1, -1, -1):
            d = int(num[i])
            tmp = d * digit + carry
            res.append(str(tmp % 10))
            carry = tmp // 10
            
        if carry > 0:
            res.append(str(carry))
            
        return ''.join(res[::-1]) + ('0' * zeros)
    
    def add(self,num1, num2):
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        N, M = len(num1), len(num2)
        carry = 0
        result = []
        for i in range(N - 1, -1, -1):
            d1, d2 = int(num1[i]), 0
            idx = i - N + M
            if idx >= 0:
                d2 = int(num2[idx])
            res = d1 + d2 + carry
            result.append(str(res % 10))
            carry = res // 10
            
        if carry > 0:
            result.append(str(carry))
            
        return ''.join(result[::-1])
            
    def multiply(self, num1: str, num2: str) -> str:
        ans = []
        N, M = len(num1), len(num2)
        num_zeros = 0
        for i in range(M - 1, -1, -1):
            ans.append(self.mul(num1, int(num2[i]), num_zeros))
            num_zeros += 1

        output = ans[0]
        for i in range(1, len(ans)):
            output = self.add(output, ans[i])
        
        idx = 0
        while idx < len(output) - 1 and output[idx] == '0':
            idx += 1
                    
        return output[idx:]