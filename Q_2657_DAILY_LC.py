class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        C=[]
        for i in range(1, len(A)+1):
            X=A[:i]
            Y=B[:i]
            Z=list(set(X+Y))
            count=0
            for j in range(len(Z)):
                if Z[j] in X and Z[j] in Y:
                    count+=1
            C.append(count)
        return C
