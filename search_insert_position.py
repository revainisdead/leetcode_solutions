from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        last_index = False

        for i, num in enumerate(nums):
            check_next = 0
            try:
                check_next = nums[i + 1]
            except IndexError:
                last_index = True

            if num == target:
                return i
            elif num < target and check_next > target:
                return i + 1
            elif num > target:
                # less than first number in list
                return 0
            elif last_index:
                return i + 1


def main():
    s = Solution()

    output = s.searchInsert([1, 3, 5, 6], 5)
    print(output)
    assert output == 2


if __name__ == "__main__":
    main()
