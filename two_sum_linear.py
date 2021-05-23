class Solution:
    mapping = {}
    nums_len = len(nums)

    for i in range(nums_len):
        nums = nums[i]

        mapping[num] = i

    for i in range(nums_len):
        num = nums[i]

        diff = target - num
        if diff in mapping:
            diff_i = mapping[diff]

            # Can't reuse the same number! Ensure indexes are different.
            if i != diff_i:
                return [i, diff_i]
