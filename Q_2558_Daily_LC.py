# TC:O(K(logn))
# SC:O(N)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-i for i in gifts]
        heapify(gifts)
        while k:
            temp = heappop(gifts)
            temp = int(abs(temp) ** (1/2))
            # print(temp)
            heappush(gifts, -temp)
            k-=1

        return -1 * sum(gifts)
