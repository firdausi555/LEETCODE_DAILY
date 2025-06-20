class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums=sorted(nums)
        ans=[]
        i=0
        while i<len(nums)-2:
            if nums[i+2]-nums[i]<=k:
                temp=[]
                for itr in range(i,i+3):
                    temp.append(nums[itr])
                ans.append(temp)
            else:
                return []
            i+=3
        return ans 
