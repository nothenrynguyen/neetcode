class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(array, L, M, R):
            
            # get left and right halves of the array
            left, right = array[L:M+1], array[M+1:R+1]

            # now we can merge them without overwriting values
            # pointers i = array, j = left half, k = right half = 0 for beginning of each subarray
            i, j, k = L, 0, 0

            # now for the actual merge
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    array[i] = left[j]
                    j += 1
                else: # if the right val was smaller
                    array[i] = right[k]
                    k += 1
                i += 1

            while j < len(left): # if the left side has leftover elements
                nums[i] = left[j]
                j += 1
                i += 1

            while k < len(right): # if the right side has leftover elements
                nums[i] = right[k]
                k += 1
                i += 1

        def mergeSort(array, l, r):
            if l == r:
                return array\

            m = (l + r) // 2
            mergeSort(array, l, m)
            mergeSort(array, m + 1, r)
            merge(array, l, m, r)
            return array

        return mergeSort(nums, 0, len(nums) - 1)