class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        longer = max(len(word1), len(word2))
        i = 0
        results = []
        for i in range(longer):
            if i < len(word1):
                results += word1[i]
            if i < len(word2):
                results += word2[i]
        results = ''.join(results)
        return results