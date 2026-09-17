class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(num, temp):
            if len(temp) == k:
                ans.append(temp[:])
                return
            
            for i in range(num, n + 1):
                temp.append(i)
                backtrack(i + 1, temp)
                temp.pop()

        backtrack(1, [])
        return ans