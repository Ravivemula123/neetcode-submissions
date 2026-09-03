class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:

        new_arr = []

        for i in nums:
            new_arr.append(i)

        nums.extend(new_arr)

        return nums
        