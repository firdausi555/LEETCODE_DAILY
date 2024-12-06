class Solution:
    def maxCount(self, banned: list[int], n: int, maxSum: int) -> int:
        bannedSet = set(banned)
        tempSum = 0
        ans = 0
        for i in range(1, n + 1):
            if i in bannedSet or tempSum + i > maxSum:
                continue
            tempSum += i
            ans += 1
        return ans
