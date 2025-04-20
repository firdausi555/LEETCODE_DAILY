class Solution:
    def numRabbits(self, answers):
        counter = Counter(answers)
        res = 0
        for ans, count in counter.items():
            if ans == 0:
                res += count
            else:
                res += math.ceil(count / (ans + 1)) * (ans + 1)
        return res
