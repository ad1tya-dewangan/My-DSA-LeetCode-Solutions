# Approach
# Sort the array, fix one element, and use two pointers to find the other two.
# shrink the pointers invard if sum matches 0
# if sum is less than 0 increase left 
# if sum is greater than 0 decrease right
# Skip duplicates to avoid repeated triplets.

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        res = []

        for i in range(n-2):
            # if we encounter positive num after sorting means other numbers
            # are also positive which can't be sum to 0 so break
            if nums[i] > 0:
                break
            
            # skip duplicate for 1st element
            if i != 0 and nums[i] == nums[i-1]:
                continue

            j = i+1
            k = n-1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                elif total == 0:
                    temp = [nums[i],nums[j],nums[k]]
                    res.append(temp)
                    j += 1
                    k -= 1
                    # similarly skip duplicate for 2nd and 3rd elements
                    # also make sure both pointers not pass ech other
                    while j<k and nums[j] == nums[j-1]:
                        j += 1
                    while j<k and nums[k] == nums[k+1]:
                        k -= 1

        return res