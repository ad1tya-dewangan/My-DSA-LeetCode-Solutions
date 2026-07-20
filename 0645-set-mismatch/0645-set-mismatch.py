class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        freq = {}
        actual_sum = 0
        repeating = 0
        
        for num in nums:
            actual_sum += num
            
            freq[num] = freq.get(num,0) + 1
            
            if freq[num] == 2:
                repeating = num
                
        expected_sum = (n*(n+1)) // 2
        
        missing = expected_sum - (actual_sum - repeating)
        
        return [repeating,missing]