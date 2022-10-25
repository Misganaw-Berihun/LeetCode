class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
        repeated = set()
        n = len(s)
        count = defaultdict(int)
        
        hash_val = 0
        cur_pow = 0
        for i in range(10):
            order = ord(s[i]) - ord('a')
            hash_val += order * pow(11, cur_pow)
            cur_pow += 1

        count[hash_val] += 1
        for i in range(10, n):
            left_order = ord(s[i - 10]) - ord('a')
            hash_val = (hash_val - left_order) // 11
            right_order = ord(s[i]) - ord('a')
            hash_val += (right_order * pow(11, 9))
            count[hash_val] += 1
            
            if count[hash_val] > 1:
                repeated.add(s[i-9: i+1])
        
        return repeated
            