from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        state = {}

        for i in range(len(nums)):
            num = nums[i]

            if not num in state.keys():
                state[num] = 1
            else:
                state[num] = state[num] + 1

        for k, val in state.items():
            if val == 1:
                return k


def main():
    s = Solution()

    # Easy: where every element appears two times, except one
    output = s.singleNumber([4, 1, 2, 1, 2])
    assert output == 4

    # Medium: where every element appears three times, except one
    output = s.singleNumber([0, 1, 0, 1, 0, 1, 99])
    assert output == 99


if __name__ == "__main__":
    main()
