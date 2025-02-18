class Solution:
    def smallestNumber(self, pattern: str) -> str:
        n=1
        stack=[]
        ans=""
        for i in pattern +'I':
            if i=='D':
                stack.append(str(n))
            else:
                ans+=str(n)
                while stack:
                    ans+=stack.pop()
            n+=1
        return ans
