from typing import List

class Solution:
    def inner_check_words(self, ch: str, strs: List[str]) -> bool:
        passes = []

        for word in strs:
            if word.startswith(ch):
                passes.append(True)
            else:
                passes.append(False)

        if all(passes):
            return True

    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Start with the first word, inner loop will check the rest, after looping word
        word = strs[0]

        sub_chs = ""
        for i in range(len(word)):
            ch = word[i] # ex. f

            # If there are no matches ever, this will end up as the return value of an empty string
            prev_sub_chs = sub_chs

            sub_chs += ch

            print(sub_chs)

            success = self.inner_check_words(sub_chs, strs)

            if success:
                continue
            else:
                return prev_sub_chs

        return sub_chs


def main():
    s = Solution()

    output = s.longestCommonPrefix(["flower", "flow", "flight"])
    assert output == "fl", "Wrong answer"


if __name__ == "__main__":
    main()
