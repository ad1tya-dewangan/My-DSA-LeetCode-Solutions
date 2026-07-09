class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0: return 0
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if num-1 not in numSet:
                currNum = num
                currLen = 1

                while currNum + 1 in numSet:
                    currNum += 1
                    currLen += 1

                longest = max(longest,currLen)

        return longest
