class Solution:
    def maximumSum(self, nums):
        dit  = {}
        res = -1

        for num in nums:
            key = self.helper(num)
            if key in dit:
                res = max(res, dit[key] + num)
                dit[key] = max(dit[key], num)
            else:
                dit[key] = num

        return res

    def helper(self, n):
        return sum(int(digit) for digit in str(n))
