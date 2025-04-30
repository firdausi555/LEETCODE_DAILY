class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans=0
        for i in nums:
            if self.helper(i):
                ans+=1
        return ans

    def helper(self, temp):
        return len(str(temp)) % 2 == 0
