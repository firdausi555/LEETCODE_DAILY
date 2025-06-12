class Solution:
    def maxAdjacentDistance(self, nums):
        n = len(nums)
        maxi = abs(nums[0] - nums[-1])
        for i in range(n - 1):
            maxi = max(maxi, abs(nums[i] - nums[i + 1]))
        return maxi
