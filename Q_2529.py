class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        return max(len([a for a in nums if a>0]),len([b for b in nums if b<0]))
