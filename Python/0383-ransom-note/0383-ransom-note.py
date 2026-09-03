class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        if len(ransomNote) > len(magazine):
            return False

        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False

        return True