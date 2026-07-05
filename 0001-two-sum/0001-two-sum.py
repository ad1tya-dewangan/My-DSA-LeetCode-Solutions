class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums[index1] + nums[index2] = target
        # then nums[index2] = target - nums[index1]

        n = len(nums)
        Map = {}
        for i in range(n):
            need = target - nums[i]
            if need in Map:
                return [Map[need],i]
            
            Map[nums[i]] = i

        return None

