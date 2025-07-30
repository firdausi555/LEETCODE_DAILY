class Solution:
    def longestSubarray(self, nums):
        temp=max(nums)
        ans=0
        counter =0
        for i in nums:
            if i==temp:
                counter+=1
            else:
                counter=0
            ans=max(ans,counter)
        return ans 
       
        
