class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def findPre(left, right):
            pre = ""
            for i in range(min(len(left), len(right))):
                if left[i] == right[i]:
                    pre += left[i]
                else:
                    break
            return pre
        
        def divideAndConcur(start, end):
            if start == end:
                return strs[start]
            mid = start + (end - start) // 2
            left_half = divideAndConcur(start, mid)
            right_half = divideAndConcur(mid + 1, end)
            return findPre(left_half, right_half)
        
        return divideAndConcur(0, len(strs) - 1)
        