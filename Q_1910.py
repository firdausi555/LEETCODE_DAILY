class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            index = s.find(part)
            if index == -1:
                break
            s = s[:index] + s[index + len(part):]
        return s
