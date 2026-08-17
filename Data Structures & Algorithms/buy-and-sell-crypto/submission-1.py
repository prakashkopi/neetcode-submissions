class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [10,1,5,6,7,1]
        maxP= 0
        l= 0
        r= 0
        for i in range(len(prices)):
            if prices[r] < prices[l]:
                l = r
            maxP= max(prices[r] - prices[l], maxP)
            r+=1

        return maxP
        