Approach 1:

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i+1, n):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    count += 1
        return count

Approach 2:

class Solution:
    def helper(self, str1: str, str2: str) -> bool:
        n1, n2 = len(str1), len(str2)
        if n1 > n2:
            return False
        return str2[:n1] == str1 and str2[-n1:] == str1

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                if self.helper(words[i], words[j]):
                    count += 1
        return count