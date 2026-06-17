class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        set1 = {}
        set2 = {}

        for element in s:
            if element in set1:
                set1[element] += 1
            else:
                set1[element] = 1

        for element in t:
            if element in set2:
                set2[element] +=1
            else :
                set2[element] = 1

        if set1 == set2:
            return True

        else:
            return False 