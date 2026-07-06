class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        half = n//2
        # Using HashMap tc : O(n) sc : O(n)
        # Map = {}    # number : frequency
        # for num in nums:
        #     Map[num] = Map.get(num,0) + 1
            
        #     if Map[num] > half:
        #         return num

        # return 0

        # Using Boyer-Moore-Voting Algo tc : O(n) sc : O(1)
        count = 0
        candidate = 0

        for num in nums:
            if count == 0:
                candidate = num

            if candidate == num:
                count += 1
            else:
                count -= 1


        return candidate
            