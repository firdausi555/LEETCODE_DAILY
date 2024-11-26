class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        degree=[0]*n
        for i,j in edges:
            degree[j]+=1
        ans=[i for i in range(n) if degree[i]==0]
        return ans[0] if len(ans)==1 else -1

        
