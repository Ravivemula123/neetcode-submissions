class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        
        first_element, second_element = 0,0

        while first_element < len(s) and second_element < len(t):

            if s[first_element] == t[second_element]:
                first_element ,second_element = first_element +1 , second_element +1
            else :
                first_element += 1

        return len(t) - second_element