class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []

        def backtrack(index):
            if index == len(nums):
                res.append(nums[:])
                return

            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                backtrack(index + 1)
                nums[i], nums[index] = nums[index], nums[i]
        
        backtrack(0)
        return res

            