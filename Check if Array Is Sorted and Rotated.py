class Solution:
    def check(self, nums: List[int]) -> bool:
        q=deque(nums)
    
        for i in range(len(nums)):
            q.rotate(1)
            if list(q)==sorted(nums):
                return True
        return False
      
