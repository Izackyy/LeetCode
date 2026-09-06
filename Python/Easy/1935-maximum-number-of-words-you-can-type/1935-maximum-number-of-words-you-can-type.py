class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        broken = set(brokenLetters)
        words = text.split(" ")
        count = 0
        for w in words:
            for ch in w:
                if ch in broken:
                    count += 1
                    break

        return len(words) - count


        
        
