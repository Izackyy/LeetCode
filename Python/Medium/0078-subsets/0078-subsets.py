class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        
        def backtrack(index, temp):
            ans.append(temp[:])

            for i in range(index, len(nums)):
                temp.append(nums[i])
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(0, [])

        return ans

