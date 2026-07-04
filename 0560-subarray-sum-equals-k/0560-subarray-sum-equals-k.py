class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)

        currSum = 0
        count = 0
        preMap = {0:1}
        # we store frequency of 0 in map because if currSum became k 
        # then currSum - k = 0
        # so we need to count the frequency of that also 
        # it also handle if index 0 has the value equal to k

        for i in range(n):
            currSum += nums[i]

            rem = currSum - k

            if rem in preMap:
                count = count + preMap[rem]

            preMap[currSum] = preMap.get(currSum,0) + 1

        return count