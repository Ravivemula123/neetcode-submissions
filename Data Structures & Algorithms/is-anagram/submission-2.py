class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        set1 = {}
        set2 = {}

        for i in range(len(s)):
            if s[i] in set1:
                set1[s[i]] += 1
            else:
                set1[s[i]] = 1 

        for i in range(len(t)):
            if t[i] in set2:
                set2[t[i]] += 1
            else:
                set2[t[i]] = 1

        if set1 == set2:
            return True 

        else:
            return False