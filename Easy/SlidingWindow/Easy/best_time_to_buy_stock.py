from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                price = prices[r] - prices[l]
                maxProfit = max(maxProfit, price)
            else:
                l = r
            
            r += 1
        return maxProfit
        
    def maxProfit2(self, prices: List[int]) -> int:
        maxProfit = 0
        minAmount = prices[0]

        for n in prices:
            maxProfit = max(maxProfit, n - minAmount)
            minAmount = min(minAmount, n)
        
        return maxProfit


solution = Solution()

data = [7, 1, 5, 3, 6, 4]
result = solution.maxProfit(data)
print(result)