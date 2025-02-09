class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        mpp = defaultdict(int)
        n = len(nums)
        
        for i in range(n):
            mpp[nums[i] - i] += 1
        
        goodPairs = sum((count * (count - 1)) // 2 for count in mpp.values())
        
        return (n * (n - 1) // 2) - goodPairs
