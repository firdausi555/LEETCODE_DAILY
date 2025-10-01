class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        ans=numBottles
        while numBottles!=0:
            temp=numBottles//numExchange
            ans+=temp
            if temp==0:
                numBottles=0
            else:
                numBottles=temp+(numBottles-(temp*numExchange))
        return ans
            





