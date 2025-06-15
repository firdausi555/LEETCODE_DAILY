class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)

        maxi = s
        for ch in s:
            if ch != '9':
                maxi = s.replace(ch, '9')
                break

        mini = s
        for ch in s:
            if ch != '0':
                mini = s.replace(ch, '0')
                break

        return int(maxi) - int(mini)
