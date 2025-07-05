from collections import Counter
from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)
        ans = []

        for num in count:
            if num == count[num]:
                ans.append(num)

        return max(ans) if ans else -1
