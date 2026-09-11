class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_max, prev_max = 0, float('-inf')

        for num in nums:
            curr_max = max(num, curr_max + num)
            prev_max = max(prev_max, curr_max)

        return prev_max