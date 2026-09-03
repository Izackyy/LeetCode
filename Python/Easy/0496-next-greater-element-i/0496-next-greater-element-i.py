class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hmap = {}
        s = []

        for num in reversed(nums2):
            while s and s[-1] <= num:
                s.pop()
            if not s:
                hmap[num] = -1
            else: 
                hmap[num] = s[-1]
            s.append(num)

        ans = []
        for num in nums1:
            ans.append(hmap[num])

        return ans
