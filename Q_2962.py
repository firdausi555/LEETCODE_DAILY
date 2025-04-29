class Solution:
    def countSubarrays(self, nums, k):
        fre = 0
        maxx = max(nums)
        left =0
        ans=0
        for right in nums:
            if right == maxx:
                fre += 1
            while fre >= k:
                if nums[left] == maxx:
                    fre -= 1
                left += 1
            ans += left
        return ans
