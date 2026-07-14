class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        maj = n // 3
        Map = {}
        res = set()
        for num in nums:
            Map[num] = Map.get(num,0) + 1

            if Map[num] > maj:
                res.add(num)

        return list(res)