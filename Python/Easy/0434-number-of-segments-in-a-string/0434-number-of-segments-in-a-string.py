class Solution(object):
    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if len(s) == 0: return 0
        # if (s.count(' ') == len(s)): return 0

        # space = 1

        # for c in s:
        #     if c == ' ':
        #         space += 1

        # return space

        return len(s.strip().split())