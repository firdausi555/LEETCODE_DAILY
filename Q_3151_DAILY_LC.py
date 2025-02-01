class Solution:
    def isArraySpecial(self, nums):
        if len(nums)==1:
            return True
        for i in range(len(nums)-1):
            if nums[i]%2==0 and nums[i+1]%2!=0:
                i+=1
            elif nums[i]%2!=0 and nums[i+1]%2==0:
                i+=1
            else:
                return False
        return True
