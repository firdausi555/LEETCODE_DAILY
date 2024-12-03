class Solution:
    def addSpaces(self,s,spaces):
        spaces=list(reversed(spaces))
        ans=""
        i=0
        while i<len(s):
            if spaces:
                if i==spaces[-1]:
                    ans+=" "
                    spaces.pop()
                else:
                    ans+=s[i]
                    i+=1
            else:
                ans+=s[i]
                i+=1
        return ans
        
