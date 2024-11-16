class Solution:

    def helper(self,temp):
        return all(temp[i]+1==temp[i+1] for i in range(len(temp)-1))

    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)-k+1
        ans=[0]*n
        for i in range(n):
            temp=nums[i:i+k]
            if self.helper(temp):
                ans[i]=max(temp)
            else:
                ans[i]=-1
        return ans
