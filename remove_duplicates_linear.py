class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # slower pointer
        i = 0

        # faster pointer
        for j in range(len(nums)):
            # not equal because that is when we update
            # the slower pointer, and then swap the values
            # of the slower pointer and faster pointer
            if nums[i] != nums[j]:
                i += 1

                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp

        # take the index of the slower pointer (full list)
        # and add 1 to get length
        return i + 1
