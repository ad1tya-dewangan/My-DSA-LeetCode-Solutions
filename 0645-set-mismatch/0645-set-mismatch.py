class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        hash_arr = [0]*(n+1)

        for num in nums:
            hash_arr[num] += 1

        missing = -1
        repeating = -1

        for i in range(1,n+1):
            if hash_arr[i] == 2:
                repeating = i
            elif hash_arr[i] == 0:
                missing = i

            if missing != -1 and repeating != -1:
                break

        return [repeating,missing]
            