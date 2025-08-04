class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
    
        maxL=0
        l=0
        r=0
        n=len(fruits)
        dit={}
        
        while r<n:
            if fruits[r] not in dit:
                dit[fruits[r]]=1
            else:
                dit[fruits[r]]+=1
            if len(set(dit))<=2:
                maxL=max(maxL,r-l+1)
                r+=1
            else:
                if dit[fruits[l]]==1:
                    dit.pop(fruits[l])
                else:
                    dit[fruits[l]]-=1
                r+=1
                l+=1
        return maxL




