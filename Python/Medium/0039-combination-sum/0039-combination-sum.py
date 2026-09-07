class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        def backtrack(index, currSum, temp):
            if index == len(candidates):
                if currSum == target:
                    ans.append(temp[:])
                return
            if currSum >= target:
                if currSum == target:
                    ans.append(temp[:])
                return
            
            temp.append(candidates[index])
            backtrack(index, currSum + candidates[index], temp)
            temp.pop()
            backtrack(index + 1, currSum, temp)

        backtrack(0, 0, [])

        return ans