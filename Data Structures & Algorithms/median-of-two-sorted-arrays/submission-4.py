class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A = nums1
        B = nums2

        total = len(nums1) + len(nums2)
        half = total // 2

        # we run binarysearch on A and make sure it's smaller
        # just for simplicity of our program

        if len(B) < len(A):
            A, B = B, A
        # now A is smaller fs

        if len(A) == 0:
            if total % 2:
                return B[half]
            return (B[half - 1] + B[half]) / 2

        left = 0
        right = len(A)

        while True:

            # now we compute middle val of A
            i = (left + right) // 2 # A
            j = half - i - 2        # B - subtract by 2 cuz index

            Aleft = A[i] if 0 <= i < len(A) else float("-infinity")
            Aright = A[i + 1] if (i + 1) < len(A) else float("infinity")

            Bleft = B[j] if j >= 0 else float("-infinity")
            Bright = B[j + 1] if (j + 1) < len(B) else float("infinity")

            # partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                
                # odd
                if total % 2:
                    return min(Aright, Bright)
                
                # even
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 # single slash for dec div

            elif Aleft > Bright:
                right = i - 1
            
            else:
                left = i + 1
