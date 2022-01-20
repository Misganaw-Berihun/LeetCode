class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = dict() #key = element in nums2    value = corresponding idx
        ans = []
        
        #recored (key,idx) of nums2
        for i,val in enumerate(nums2):
            d[val] = i
        
        for elem in nums1:#for each element of nums1
            idx = d[elem] #find elem's index in nums2
            k = idx + 1 #k holds index of elements beyond idx
            
            while k < len(nums2) and nums2[idx] >= nums2[k]: #loop until last or 
                                                        #find val greater than nums[idx]
                k += 1
                
            if k == len(nums2): #if value greater not found
                ans.append(-1)
            else:#if value found
                ans.append(nums2[k])
                
        return ans
            
        
