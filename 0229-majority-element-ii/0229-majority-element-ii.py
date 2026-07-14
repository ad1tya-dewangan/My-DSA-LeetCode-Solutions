# Uses Boyer-Moore Majority Vote algorithm to find elements appearing > n // 3 times.
# Phase 1: Tracks up to 2 potential candidates by pairing out 3 distinct elements.
# Phase 2: Verifies candidates with a second pass to check if their actual counts exceed the threshold.

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        count1 = count2 = 0

        # Identify potential candidates
        for num in nums:
            if cand1 == num:
                count1 += 1
            elif cand2 == num:
                count2 += 1
            elif count1 == 0:
                cand1 = num
                count1 = 1
            elif count2 == 0:
                cand2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        # Verify the candidates
        count1 = count2 = 0
        for num in nums:
            if cand1 == num: count1 += 1
            if cand2 == num: count2 += 1

        res = []
        maj = len(nums) // 3

        if count1 > maj: res.append(cand1)
        if count2 > maj: res.append(cand2)

        return res