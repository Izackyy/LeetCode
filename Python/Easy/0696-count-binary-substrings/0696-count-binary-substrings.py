class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        prev = 0
        streak = 1
        ans = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]: 
                streak += 1
            else:
                prev = streak
                streak = 1
            
            if streak <= prev:
                ans += 1

        return ans

