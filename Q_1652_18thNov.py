class Solution:
    def decrypt(self, code, k):
        ans=[0]*len(code)
        for i in range(len(code)):
            if k>0:
                for j in range(i+1,i+1+k):
                    ans[i]+= code[j%len(code)]
            else:
                for j in range(i-1,i-abs(k)-1,-1):
                    ans[i]+=code[j%len(code)]
        return ans
