class Solution:
    def maxScore(self, s: str) -> int:
        one=s.count('1')
        zero=0
        ans=0

        for i in range(len(s)-1):
            if s[i]=='0':
                zero+=1
            else:
                one-=1
            ans=max(ans,zero+one)
        return ans
