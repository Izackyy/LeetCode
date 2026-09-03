class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first, count = {}, {}
        ans, degree = 0, 0

        for i, n in enumerate(nums):
            first.setdefault(n, i)
            count[n] = count.get(n, 0) + 1

            if count[n] > degree:
                degree = count[n]
                ans = i - first[n] + 1
            elif count[n] == degree:
                ans = min(ans, i - first[n] + 1)
            
        return ans
