class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counts = {}
        rLen, mLen = len(ransomNote), len(magazine)
        for ch in magazine:
            if ch in counts:
                counts[ch] += 1
            else:
                counts[ch] = 1
        for ch in ransomNote:
            if ch not in counts:
                return False
            counts[ch] -= 1
            if counts[ch] < 0:
                return False
        return True
