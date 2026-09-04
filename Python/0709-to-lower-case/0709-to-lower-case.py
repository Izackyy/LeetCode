class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                ans += chr(ord(s[i]) + 32)
            else:
                ans += s[i]

        return ans
