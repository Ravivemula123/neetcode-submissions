class Solution:
    def getConcatenation(self,nums):

        res = []
        for i in nums:
            res.append(i)

        nums.extend(res)

        return nums

