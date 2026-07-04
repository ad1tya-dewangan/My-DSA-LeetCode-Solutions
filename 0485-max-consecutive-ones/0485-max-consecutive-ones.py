class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        currMax = 0
        for i in range(n):
            if nums[i] == 1:
                count += 1
                currMax = max(currMax,count)
            else:
                count = 0

        return currMax