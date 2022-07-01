class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb = [0 for i in range(target + 1)]
        comb[0] = 1
        for i in range(target + 1):
            if comb[i] != 0:
                for num in nums:
                    if i + num <=  target:
                        comb[i + num] += comb[i]
        return comb[target]