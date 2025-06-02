class Solution:
    def candy(self, ratings: List[int]) -> int:
        n=len(ratings)
        ans=n*[1]

        # for left pass 
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                ans[i]=ans[i-1]+1
        # for right pass 
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                ans[i]=max(ans[i],ans[i+1]+1)
        

        return sum(ans)
