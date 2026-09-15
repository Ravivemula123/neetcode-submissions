class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:


        if len(strs) == 0:
            return [[]]

        if len(strs) == 1:

            return [strs]

        data = {}

        for i in strs:

            value = "".join(sorted(i))

            if value in data:
                data[value].append(i)

            else:
                data[value] =[i]


        result = list(data.values())

        result.reverse()

        return result        