import collections
class Solution:
  def tupleSameProduct(self, nums):
    
    ans = 0
    count = collections.Counter()

    for i in range(len(nums)):
      for j in range(i):
        prod = nums[i] * nums[j]
        ans += count[prod] * 8
        count[prod] += 1

    return ans
obj=Solution()
obj.tupleSameProduct(nums= [2,3,4,6])
