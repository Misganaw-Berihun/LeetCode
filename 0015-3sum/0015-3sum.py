class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        output = set()
        for i in range(len(nums)):
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                if (i == left):
                    left = left + 1
                elif (i == right):
                    right = right - 1
                else:
                    temp = nums[left] + nums[right]
                    if (temp == target):
                        cont = sorted([-target, nums[left], nums[right]])
                        output.add(tuple(cont))
                        left = left + 1
                        right = right - 1
                    elif (temp < target):
                        left = left + 1
                    elif (temp > target):
                        right = right - 1
        return output