class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        result = ""

        for index in range(len(strs[0])):

            for element in strs:

                if index == len(element) or element[index] != strs[0][index]:
                    return result

            result += strs[0][index]

        return result