class Solution:
    def countLargestGroup(self, n: int) -> int:
        dit = {}
        
        for i in range(1, n + 1):
            s = self.helper(i)
            if s in dit:
                dit[s] += 1
            else:
                dit[s] = 1
        
        max_size = max(dit.values())
        return sum(1 for v in dit.values() if v == max_size)

    def helper(self, n: int) -> int:
        total = 0
        while n:
            total += n % 10
            n //= 10
        return total
