class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:

        num1ZeroCount=nums1.count(0)
        num2ZeroCount=nums2.count(0)
        num1Sum=sum(nums1)+num1ZeroCount
        num2Sum=sum(nums2)+num2ZeroCount

        if num1ZeroCount == 0 and num2Sum > num1Sum:
            return -1

        if num2ZeroCount==0 and num1Sum > num2Sum:
            return -1


           
        return max(num1Sum,num2Sum)
