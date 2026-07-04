class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # sum approach
        # expSum = n*(n+1) // 2
        # actualSum = 0
        # for num in nums:
        #     actualSum += num

        # return expSum - actualSum

        # XOR Approach

        xor1 = n
        xor2 = 0
        for i in range(n):
            xor1 = xor1 ^ i
            xor2 = xor2 ^ nums[i]

        return xor1 ^ xor2
        


            
        