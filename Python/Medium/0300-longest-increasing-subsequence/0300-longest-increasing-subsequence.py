class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = []

        for num in nums:
            if len(temp) == 0 or temp[-1] < num:
                temp.append(num)
            else:
                i = bisect_left(temp, num)
                temp[i] = num

        return len(temp)
