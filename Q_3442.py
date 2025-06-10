class Solution:
    def maxDifference(self, s: str) -> int:
        c=Counter(s)
        o=[]
        e=[]
        for i in c.values():
            if i%2==0:
                e.append(i)
            else:
                o.append(i) 
        odd=sorted(o)
        even=sorted(e)
        return (odd[-1]-even[0])
