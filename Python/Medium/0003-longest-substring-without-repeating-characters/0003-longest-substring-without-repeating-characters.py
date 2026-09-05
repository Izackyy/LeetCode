class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_map = {}
        l = 0
        length = 0

        for r in range(len(s)):
            
            if s[r] in char_map:
                l = max(l, char_map[s[r]] + 1)
            char_map[s[r]] = r
            length = max(length, r - l + 1)

        return length