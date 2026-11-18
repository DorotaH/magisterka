class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        total_profit = 0
        profit = 0
        min_price = prices[0]
        last_price = prices[0]
        for price in prices[1::]:
            #print(f'price: {price}')
            #print(f'min_price: {min_price}')
            #print(f'total_profit: {total_profit}')

            if price <= last_price:

                min_price = price
                total_profit = profit + total_profit
                profit = 0
            else:
                profit = max(profit, price - min_price)
                print(profit)
            last_price = price
        return profit + total_profit
