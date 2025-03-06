class Solution:
    def findMissingAndRepeatedValues(self, grid):

        new=[]
        result=[]
        for i in grid:
            new.extend(i)
        for i in new:
            if new.count(i)==2:
                duplicate=i
        for i in range(1,len(new)+1):
            if i not in new:
                missing=i
        result.append(duplicate)
        result.append(missing)
        return result
