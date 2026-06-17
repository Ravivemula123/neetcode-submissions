class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        
        result = len(s.split()[-1])

        return result