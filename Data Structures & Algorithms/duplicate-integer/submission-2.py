class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        new_arr = list(set(nums))

        if len(nums) == len(new_arr):
            return False
        else:
            return True


            
        