class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        ans=0
        temp=0
        left=0
        for right in range(len(nums)):
            temp+=nums[right]
            while temp * (right-left +1 ) >=k:
                temp-=nums[left]
                left+=1
            ans+=right-left+1
        return ans
