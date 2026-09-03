class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        oddCount = 0
        m = {}

        for c in s:
            m[c] = m.get(c, 0) + 1
            if m[c] % 2 == 1:
                oddCount += 1
            else:
                oddCount -= 1
            
        if oddCount > 1:
            return len(s) - oddCount + 1
        else:
            return len(s)
