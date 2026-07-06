class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        half = n//2
        Map = {}    # number : frequency

        for num in nums:
            Map[num] = Map.get(num,0) + 1
            
            if Map[num] > half:
                return num

        return None