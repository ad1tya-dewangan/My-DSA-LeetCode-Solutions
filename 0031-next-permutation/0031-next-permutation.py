"""
INTUITION FOR NEXT PERMUTATION (Lexicographically Next Greater Sequence):
To find the next slightly larger number, we must change the sequence as far right as possible.

1. FIND THE BREAK: Scan from right to left to find the first element that drops in value 
   (nums[i] < nums[i+1]). This index 'i' is our pivot. Everything to its right is decreasing.
   
2. EDGE CASE (MAX PERMUTATION): If no such drop is found (index == -1), the array is entirely 
   descending (e.g., [3,2,1]). Reverse it completely to reset to the smallest order [1,2,3] and exit.
   
3. FIND SUCCESSOR & SWAP: If a pivot is found, scan from right to left again to find the first 
   element strictly greater than nums[pivot]. Swap them. This slightly increases the prefix value.
   
4. MINIMIZE THE SUFFIX: The elements to the right of the pivot are still in descending order. 
   To make this new sequence as small as possible, reverse this suffix into ascending order.
"""

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def revArray(arr,left,right): #helper function
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -= 1

        n = len(nums)
        index = -1
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                index = i
                break

        if index == -1:
            revArray(nums,0,n-1)
            return 

        for j in range(n-1,index,-1):
            if nums[j] > nums[index]:
                nums[j],nums[index] = nums[index],nums[j]
                break
        
        revArray(nums,index+1,n-1)
        