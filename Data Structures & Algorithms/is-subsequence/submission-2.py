class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        first_element ,second_element = 0,0

        while first_element <len(s) and second_element < len(t):

            if s[first_element] == t[second_element]:
                first_element +=1

            second_element +=1

        return True if first_element == len(s) else False