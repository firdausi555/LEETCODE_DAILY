class Solution:
    def maxFreqSum(self, s: str) -> int:
        temp = "aeiou"
        vol = [i for i in s if i in temp]
        cons = [i for i in s if i not in temp]

        count1 = Counter(vol)
        count2 = Counter(cons)

        max_vowel = max(count1.values(), default=0)
        max_cons  = max(count2.values(), default=0)

        return max_vowel + max_cons
