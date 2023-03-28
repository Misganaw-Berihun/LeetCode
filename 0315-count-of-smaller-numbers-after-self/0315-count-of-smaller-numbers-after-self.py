class Solution:
    def merge(self, nums, left, mid, right):
        p1, p2 = left, mid + 1
        
        while p1 <= mid:
            while p2 <= right and nums[p1][0] > nums[p2][0]:
                p2 += 1
            
            self.count[nums[p1][1]] += (p2 - mid - 1)
            p1 += 1
        
        p1, p2 = left, mid + 1
        new = []
        while p1 <= mid or p2 <= right:
            if p1 > mid or (p2 <= right and nums[p2][0] < nums[p1][0]):
                new.append(nums[p2])
                p2 += 1
            else:
                new.append(nums[p1])
                p1 += 1
        
        for i in range(len(new)):
            nums[left] = new[i]
            left += 1
    
    def mergeSort(self, nums, left, right):
        if left == right:
            return
        
        mid = (left + right) // 2
        self.mergeSort(nums, left, mid)
        self.mergeSort(nums, mid + 1, right)
        self.merge(nums, left, mid, right)
        
    def countSmaller(self, nums: List[int]) -> List[int]:
        n = len(nums)
        self.count = [0 for i in range(n)]
        new_list = [(nums[i], i) for i in range(n)]
        
        self.mergeSort(new_list, 0, n - 1)
        return self.count
        
        
        