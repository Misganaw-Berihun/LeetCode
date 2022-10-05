class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
    
        left,  right,prev_com, ans = 0, 1, 0, 1
        while right <  n:
            if arr[right] < arr[right - 1]  and (prev_com == 0 or prev_com == 2):
                ans = max(ans, right - left + 1)
                prev_com = 1
            elif arr[right] > arr[right - 1] and (prev_com == 0 or prev_com == 1):
                ans = max(ans, right - left + 1)
                prev_com = 2
            else:
                if arr[right] != arr[right - 1]:
                    left = right - 1
                    prev_com = 3 - prev_com
                    continue
                left = right
            right += 1
        return ans
                