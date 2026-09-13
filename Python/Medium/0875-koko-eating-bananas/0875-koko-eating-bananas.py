class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        low, high = 1, max(piles)

        while low < high:
            mid = (low + high) // 2

            if sum((p + mid - 1) // mid for p in piles) <= h:
                high = mid
            else:
                low = mid + 1

        return low