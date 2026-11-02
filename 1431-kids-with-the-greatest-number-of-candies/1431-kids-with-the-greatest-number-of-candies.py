class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
      kid_with_most_candies = candies[0]
      result = []
      for i in range(len(candies)):
        if candies[i] >= kid_with_most_candies:
            kid_with_most_candies = candies[i]
      for i in range(len(candies)):
        if candies[i] + extraCandies >= kid_with_most_candies:
            result.append(True)
        else:
            result.append(False)
      return result