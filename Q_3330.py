class Solution:
    def possibleStringCount(self, word: str) -> int:
        ans = len(word)
        for i in range(1, len(word)):
            if word[i] != word[i - 1]:
                ans -= 1
        return ans
