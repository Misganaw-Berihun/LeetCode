class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        idx = len(nums1) - 1
        ptr1 = len(nums1) - len(nums2) - 1
        ptr2 = len(nums2) - 1
        
        while idx >= 0 and ptr1 >= 0 and ptr2 >= 0:
            if nums1[ptr1] > nums2[ptr2]:
                nums1[idx] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[idx] = nums2[ptr2]
                ptr2 -= 1
            idx -= 1
        while ptr2 >= 0:
            nums1[idx] = nums2[ptr2]
            ptr2 -= 1
            idx -= 1
