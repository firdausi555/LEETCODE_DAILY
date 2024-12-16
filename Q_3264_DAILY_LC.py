class Solution:
    def getFinalState(self, nums, k, multiplier):
        temp=[(j,i) for i , j in enumerate(nums)]
        heapify(temp)
        while k:
            j,i=temp[0]
            heapreplace(temp,(j*multiplier,i))
            k-=1
        for j , i in temp:
            nums[i]=j
        return nums
