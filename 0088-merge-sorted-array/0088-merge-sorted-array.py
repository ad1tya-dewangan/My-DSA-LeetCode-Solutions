# Start from the end of both arrays.
# Compare the largest remaining elements.
# Place the larger one at the end of nums1.
# Continue until one array is exhausted.
# Copy any remaining elements from nums2.
# Remaining elements in nums1 are already in the correct position.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1 
        k = (m+n) - 1

        while j >= 0 and i >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        # copy remaining elements from nums2 if any
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1
    