class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                skip_L = s[l + 1 : r + 1]
                skip_R = s[l : r]
                return skip_L == skip_L[::-1] or skip_R == skip_R[::-1]  
            
            l += 1
            r -= 1

        return True