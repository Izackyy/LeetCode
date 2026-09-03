class Solution(object):
    def licenseKeyFormatting(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        s = s.replace('-','').upper()
        n = len(s)
        firstGroup = len(s) % k or k
        ans = [s[: firstGroup]]
        
        for i in range(firstGroup, n, k):
            ans.append(s[i : i + k])
        
        return '-'.join(ans)


