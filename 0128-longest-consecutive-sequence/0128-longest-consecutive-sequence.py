class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n = len(nums)
        nums.sort()
        maxLen = 1
        currLen = 1
        for i in range(1,n):
            if nums[i] == nums[i-1]:
                continue

            if nums[i] == nums[i-1] + 1:
                currLen += 1
            else:
                maxLen = max(maxLen,currLen)
                currLen = 1
            
        maxLen = max(maxLen,currLen)

        return maxLen