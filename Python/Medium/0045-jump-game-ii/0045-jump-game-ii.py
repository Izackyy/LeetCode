class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [float('inf')] * n
        dp[n - 1] = 0

        for i in range(n - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                dp[i] = min(dp[i], 1 + dp[min(n - 1, i + j)])

        return dp[0]

