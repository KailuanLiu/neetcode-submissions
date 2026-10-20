class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        
        max_profit = 0
        min_buy = prices[0]
        for price in prices:
            # if the minimum buy > the price to buy
            if min_buy > price:
                # minimum buy becomes the price that is lower
                min_buy = price
            # if the price right now minus min_buy is 
            # greater than the max_profit 
            elif price - min_buy > max_profit: 
                # the max_profit is that new equation
                max_profit = price - min_buy
        return max_profit

