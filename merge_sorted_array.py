class Solution:
    def merge(self, nums1, m, nums2, n):
        nums1[:] = sorted(nums1[:m] + nums2[:n])

        return nums1




def main():
    def last_non_zero(arr):
        for i, num in enumerate(arr):
            if num == 0:
                # i here is the length where there were still numbers
                return i

    s = Solution()

    arr1 = [1, 2, 3, 0, 0, 0]
    arr2 = [2, 5, 6]
    output = s.merge(arr1, last_non_zero(arr1), arr2, len(arr2))
    print(output)

    assert output == [1, 2, 2, 3, 5, 6]


if __name__ == "__main__":
    main()
