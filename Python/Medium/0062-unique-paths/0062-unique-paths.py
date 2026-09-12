import math

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        numerator = math.factorial(m + n - 2)
        denominator = math.factorial(m - 1) * math.factorial(n - 1)

        return numerator / denominator