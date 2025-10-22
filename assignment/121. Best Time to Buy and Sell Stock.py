class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0

        l, r = 0, 1  # l = buy , r = sell
        maxP = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                currentP = prices[r] - prices[l]
                maxP = max(maxP, currentP)
            else:
                
                l = r
            r += 1

        return maxP

maxProfitSolution = Solution()
prices = [7, 1, 5, 3, 6, 4]
print(maxProfitSolution.maxProfit(prices))
