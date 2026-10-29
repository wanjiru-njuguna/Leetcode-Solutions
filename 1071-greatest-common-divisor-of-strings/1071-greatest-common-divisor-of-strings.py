class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        shortest = min(str1, str2)
        longest = max (str1, str2)
        initial_shortest = min(str1, str2)
        max_length = len(longest)
        min_length = len (initial_shortest)
        while shortest:
            len_shortest = len (shortest)
            if max_length % len_shortest == 0 and min_length % len_shortest == 0:
                number_fits_longer = int(max_length / len_shortest)
                number_fits_shorter = int(min_length /len_shortest )
                if shortest * number_fits_longer ==longest and shortest * number_fits_shorter == initial_shortest:
                    return(shortest)
            shortest = shortest[: -1]
        return ''