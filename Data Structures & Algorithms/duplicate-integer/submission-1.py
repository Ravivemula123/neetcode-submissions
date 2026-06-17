class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        seen = {}

        for element in nums:
            if element in seen and seen[element] >= 1:
                return True

            else :
                seen[element] = 1

        return False
