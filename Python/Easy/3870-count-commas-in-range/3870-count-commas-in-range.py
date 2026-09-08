class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        return n - 999 if n >= 1000 else 0