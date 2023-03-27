class Solution:
    def merge(self, arr, left, mid, right, diff):
        new_list = []
        p1,p2 = left, mid + 1
        
        while p1 <= mid:
            while p2 <= right and arr[p1] > arr[p2] + diff:
                p2 += 1
            
            self.count += (right - p2 + 1)
            p1 += 1
        
        p1, p2 = left, mid + 1
        while p1 <= mid or p2 <= right:
            if p2 == right + 1 or (p1 <= mid and arr[p1] < arr[p2]):
                new_list.append(arr[p1])
                p1 += 1
            else:
                new_list.append(arr[p2])
                p2 += 1
        
        p1 = left
        for i in range(len(new_list)):
            arr[p1] = new_list[i]
            p1 += 1
        
    def mergeSort(self,arr,left, right, diff):
        if left == right:
            return 
        
        mid = (left + right) // 2
        self.mergeSort(arr, left, mid, diff)
        self.mergeSort(arr, mid + 1, right, diff)
        self.merge(arr, left, mid,  right, diff)
        
        
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        new_arr = []
        
        for i in range(n):
            new_arr.append(nums1[i] - nums2[i])
        
        self.count = 0
        self.mergeSort(new_arr, 0, n - 1, diff)
        return self.count