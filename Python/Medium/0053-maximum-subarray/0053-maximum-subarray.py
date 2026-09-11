class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total = 0
        res = nums[0]

        for num in nums:
            if total < 0:
                total = 0
            
            total += num
            res = max(total, res)

        return res