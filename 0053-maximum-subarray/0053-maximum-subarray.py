class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        maxSum = float('-inf')
        arrSum = 0

        if n == 1: return nums[0]

        for i in range(n):
            if arrSum < 0:
                arrSum = 0
            
            arrSum += nums[i]
            maxSum = max(maxSum,arrSum)

        return maxSum