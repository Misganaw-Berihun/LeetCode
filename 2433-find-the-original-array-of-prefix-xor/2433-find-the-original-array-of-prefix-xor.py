class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        ans = [pref[0]]
        ans_xor = [pref[0]]
        size = len(pref)
        
        for i in range(1, size):
            cur = pref[i]
            ans.append(ans_xor[-1] ^ cur)
            ans_xor.append(ans_xor[-1] ^ ans[-1])
        
        return ans