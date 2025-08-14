class Solution:
    def largestGoodInteger(self, num: str) -> str:
        count=0
        prev=''
        ans=''
        for i in num:
            if i==prev: count+=1
            else: count=1
            if count==3:
                ans=max(i, ans)
            prev=i
        return ans*3
