class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        c=Counter(nums)
        maxi=max(c.values())
        count=0
        
        for i in c.items():
            if i[1] == maxi:
                count+=i[1]
        return count
