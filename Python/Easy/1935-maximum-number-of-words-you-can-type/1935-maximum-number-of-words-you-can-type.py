class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        return sum(not set(w) & set(brokenLetters) for w in text.split())

        
        
