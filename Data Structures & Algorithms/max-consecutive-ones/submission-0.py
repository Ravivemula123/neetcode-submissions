class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        count1, count2 = 0,0

        for element in nums:

            if element == 1:
                count1 += 1

            else:
                if count2 < count1:
                    count2 = count1
                    count1 = 0
                else :
                    count1 =0

        return max(count2,count1)