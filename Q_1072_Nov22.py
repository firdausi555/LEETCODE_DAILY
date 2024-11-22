class Solution:
    def maxEqualRowsAfterFlips(self, matrix):
        mpp=defaultdict(int)
        for row in matrix:
            row_key=tuple(row)
            if row[0]:
                row_key=tuple([0 if n else 1 for n in row])
            mpp[row_key]+=1
        return max(mpp.values())
