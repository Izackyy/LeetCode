class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        seen = collections.defaultdict(int)
        seen[0] = 1
        s, res = 0, 0

        for num in nums:
            s += num
            res += seen[s - k]
            seen[s] += 1
        
        return res