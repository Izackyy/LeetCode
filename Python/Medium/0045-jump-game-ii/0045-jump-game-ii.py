class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)        
        jumps = 0
        curr_end = 0
        far = 0
        

        for i in range(n - 1):
            far = max(far, i + nums[i])

            if (i == curr_end):
                jumps += 1
                curr_end = far

                if curr_end == n - 1:
                    break
        
        return jumps