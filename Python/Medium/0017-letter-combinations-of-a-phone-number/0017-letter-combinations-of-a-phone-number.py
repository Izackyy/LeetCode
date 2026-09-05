class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0: return []

        hmap = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        ans = []

        def backtrack(comb):
            if len(comb) == len(digits):
                ans.append(comb)
                return
            for ch in hmap[digits[len(comb)]]:
                backtrack(comb + ch)

        backtrack("")

        return ans




        