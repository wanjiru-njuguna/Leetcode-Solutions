class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0
        i = 0
        n = len(nums)
        for i in range(n):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
                i += 1
        for j in range(non_zero_index , n):
            nums[j] = 0
       