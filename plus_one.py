from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # [1, 2, 3]
        # ["1", "2", "3"]
        # "123"
        # 123
        # 124
        # "124"
        # [1, 2, 4]

        # [1, 2, 3] -> ["1", "2", "3"]
        digitsStr = [str(x) for x in digits]

        # ["1", "2", "3"] -> "123" -> 123
        digitsInt = int("".join(digitsStr))

        # 123 -> 124
        digitsInt += 1

        # 124 -> "124"
        digitsStr = str(digitsInt)

        # "124" -> [1, 2, 4]
        return [int(x) for x in digitsStr]


def main():
    s = Solution()
    output = s.plusOne([1, 2, 3])
    assert output == [1, 2, 4]

    output2 = s.plusOne([4, 3, 2, 1])
    assert output2 == [4, 3, 2, 2]


if __name__ == "__main__":
    main()
