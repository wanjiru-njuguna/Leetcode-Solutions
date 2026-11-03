class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                left_fb_empty = (i == 0) or (flowerbed[i - 1] == 0)
                right_fb_empty = (i == len(flowerbed) -1) or (flowerbed[i +1] == 0)
                if left_fb_empty and right_fb_empty:
                    flowerbed[i] = 1
                    count += 1
        return count >= n