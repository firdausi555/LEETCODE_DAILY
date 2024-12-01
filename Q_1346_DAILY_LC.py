class Solution(object):
    def checkIfExist(self, arr):
        for i in range(len(arr)):
            for j in range(len(arr)-1,-1,-1):
                if arr[i]==2*arr[j] and i!=j:
                    return True 
        return False
