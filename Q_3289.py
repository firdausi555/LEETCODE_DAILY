class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        counter=Counter(nums)
        ans=[]
        for i in counter.items():
            if i[1]==2:
                ans.append(i[0])
        return ans 
