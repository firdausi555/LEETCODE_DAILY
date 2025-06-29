class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9 + 7
        i, j = 0, len(nums) - 1
        ans = 0
        
        while i <= j:
            if nums[i] + nums[j] <= target:
                # Directly compute 2^(j - i) % mod
                ans = (ans + pow(2, j - i, mod)) % mod
                i += 1
            else:
                j -= 1
        
        return ans
