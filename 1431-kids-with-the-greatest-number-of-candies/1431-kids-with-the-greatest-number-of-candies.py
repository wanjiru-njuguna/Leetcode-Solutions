class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        #find the kid with the most candies. Assume that the first is the max then compare
        most_candies = candies[0]
        results = []
        for i in range(1,len(candies)):
            if candies[i] >= most_candies:
                most_candies = candies[i]
               
        for i in range(len(candies)):
            if candies[i] + extraCandies >= most_candies:
                results.append(True)
            else:
                results.append(False)
        return results