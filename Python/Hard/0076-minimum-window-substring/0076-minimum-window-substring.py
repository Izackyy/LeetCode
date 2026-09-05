class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if len(t) == 0 or len(t) > len(s):
            return ""

        count_t, window = {}, {}
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1

        have, need = 0, len(count_t)
        res = [-1, -1]
        res_length = float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:
                if (r - l + 1) < res_length:
                    res = [l, r]
                    res_length = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        if res_length < float('inf'):
            return s[l:r + 1]
        else:
            return ""

        