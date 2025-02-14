class ProductOfNumbers:
    def __init__(self):
        self.ans = [1]

    def add(self, num: int):
        if num == 0:
            self.ans = [1] 
        else:
            self.ans.append(self.ans[-1] * num) 

    def getProduct(self, k: int) -> int:
        if k >= len(self.ans): 
            return 0 

        return self.ans[-1] // self.ans[-k - 1] 
