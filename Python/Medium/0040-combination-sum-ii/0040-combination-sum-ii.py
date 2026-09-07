class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        candidates.sort()

        def backtrack(target, start, temp):
            if target < 0: 
                return
            if target == 0:
                ans.append(temp)
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if candidates[i] > target:
                    break
                backtrack(target - candidates[i], i + 1, temp + [candidates[i]])
            return
            
        backtrack(target, 0, [])

        return ans
            