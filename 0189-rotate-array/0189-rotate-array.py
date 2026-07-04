class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        # helper function to reverse array 
        def rev(arr,l,r):
            while l < r:
                arr[l],arr[r] = arr[r],arr[l]
                l += 1
                r -= 1

        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)
        