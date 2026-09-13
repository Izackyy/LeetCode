class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()

        mid = len(nums) // 2

        if len(nums) % 2: 
            return float(nums[mid])
        else:
            return (nums[mid - 1] + nums[mid]) / 2.0