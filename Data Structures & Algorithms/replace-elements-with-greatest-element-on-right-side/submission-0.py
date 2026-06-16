class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        length=len(arr)
        new_array = [0] * length

        for i in range(length):
            if not arr[i+1:]:
                break

            new_array[i] = max(arr[i+1:])

        new_array[-1] = -1

        return new_array


            
