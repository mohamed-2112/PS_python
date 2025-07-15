class Solution(object):
    def __init__(self):
        pass

    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.strip().split()
        return len(words[-1]) if words else 0
        