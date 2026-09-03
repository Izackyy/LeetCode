class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxLength = currLength = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                currLength += 1
                maxLength = max(maxLength, currLength)
            else: 
                currLength = 1
        return maxLength