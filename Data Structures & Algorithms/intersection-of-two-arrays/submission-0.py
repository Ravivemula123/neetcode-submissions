class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        arr = set()

        for i in nums1:
            if i in nums2:
                arr.add(i)

        return list(arr)

        

