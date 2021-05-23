from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]

            for j in range(i + 1, len(nums)):
                num2 = nums[j]

                ans = num1 + num2
                if ans == target:
                    return [i, j]

