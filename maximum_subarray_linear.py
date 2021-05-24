from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        largest = current = nums[0]

        for num in nums[1:]:
            extend = current + num

            current = max(num, extend)
            largest = max(largest, current)

        return largest


def main():
    s = Solution()
    output = s.maxSubArray([5, 4, -1, 7, 8])
    assert output == 23


if __name__ == "__main__":
    main()
