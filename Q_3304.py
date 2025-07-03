class Solution:
    def kthCharacter(self, k: int) -> str:
        ans = ['a']
        while len(ans) < k:
            size = len(ans)
            for i in range(size):
                next_char = chr(ord('a') + ((ord(ans[i]) - ord('a') + 1) % 26))
                ans.append(next_char)
        return ans[k - 1]
