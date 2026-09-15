class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        data = {}

        for i in nums:

            if i in data :
                data[i] += 1
            else:
                data[i] = 1

        key = max(data,key = data.get)

        return key        