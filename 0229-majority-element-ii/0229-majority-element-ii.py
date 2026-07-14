class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        count1 = count2 = 0

        for num in nums:
            if c1 == num:
                count1 += 1
            elif c2 == num:
                count2 += 1
            elif count1 == 0:
                c1 = num
                count1 = 1
            elif count2 == 0:
                c2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        count1 = count2 = 0

        for num in nums:
            if c1 == num: count1 += 1
            if c2 == num: count2 += 1

        res = []
        maj = len(nums) // 3

        if count1 > maj: res.append(c1)
        if count2 > maj: res.append(c2)

        return res