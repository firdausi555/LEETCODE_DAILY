class Solution:
    def sortColors(self, nums):
        start=0
        mid=0
        end=len(nums)-1
        while mid<=end:
            if nums[mid]==0:
                nums[start],nums[mid]=nums[mid],nums[start]
                mid+=1
                start+=1
            elif nums[mid]==1:
                mid+=1
            elif nums[mid]==2:
                nums[mid],nums[end]=nums[end],nums[mid]
                end-=1
        return nums
    
    
    
obj=Solution()
obj.sortColors(nums = [2,0,2,1,1,0])
