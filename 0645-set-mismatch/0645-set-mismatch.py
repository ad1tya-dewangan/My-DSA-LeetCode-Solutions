class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # actual sum and square sum of numbers in array
        S = 0
        S2 = 0

        for num in nums:
            S += num
            S2 += num * num 

        # expected sum and square sum of n number
        Sn = (n*(n+1)) // 2 
        S2n = (n*(n+1)*(2*n+1)) // 6

        # Suppose x is repeating and y is missing
        val1 = S - Sn    # x - y   --> eq.(1)
        val2 = S2 - S2n 

        val2 = val2 // val1  # x + y   --> eq.(2)

        #Add eq. (1) & (2) and we get x = val1 + val2 // 2
        repeating = (val1 + val2) // 2
        
        # from eq.(1) y = x - val1
        missing = repeating - val1

        return [repeating,missing]






        
