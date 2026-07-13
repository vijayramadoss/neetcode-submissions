class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp=0
        i,j=0,1
        while j<len(prices):
            if prices[j]<prices[i]:
                i=j
            else:
                maxp=max(maxp,prices[j]-prices[i])
            j+=1
        return maxp