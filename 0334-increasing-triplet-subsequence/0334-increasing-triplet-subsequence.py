class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        smallest = float("inf")
        second_smallest = float ("inf")
        for n in nums:
            if n <= smallest:
                smallest = n
            elif n <= second_smallest:
                second_smallest = n
            else:
                return True
        return False
        