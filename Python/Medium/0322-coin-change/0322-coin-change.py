class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0] + [float('inf')] * amount

        for amt in range(1, amount + 1):
            for c in coins:
                if c <= amt:
                    dp[amt] = min(dp[amt], dp[amt - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1