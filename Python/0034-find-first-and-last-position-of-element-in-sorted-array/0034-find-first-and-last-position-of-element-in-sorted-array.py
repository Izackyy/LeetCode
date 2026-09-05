class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def binarySearch (nums, target, is_searching_left):
            l, r = 0, len(nums) - 1
            index = -1

            while l <= r:
                mid = (l + r) // 2

                if target > nums[mid]:
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:
                    index = mid
                    if is_searching_left:
                        r = mid - 1
                    else: 
                        l = mid + 1
            return index

        l = binarySearch(nums, target, True)
        r = binarySearch(nums, target, False)

        return [l, r]