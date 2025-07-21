class Solution:
    def makeFancyString(self, s: str) -> str:
        ans = []
        for i in s:
            if len(ans) >= 2 and ans[-1] == i and ans[-2] == i:
                continue
            ans.append(i)
        return ''.join(ans)
