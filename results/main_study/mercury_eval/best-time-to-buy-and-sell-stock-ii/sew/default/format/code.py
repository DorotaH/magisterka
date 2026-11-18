class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        print(prices)
        total_profit = profit = 0
        min_price = prices[0]
        last_price = prices[0]
        for price in prices[1::]:
            # print(f'price: {price}')
            # print(f'min_price: {min_price}')
            # print(f'total_profit: {total_profit}')

            if not price <= last_price:
                if price - min_price > profit:
                    profit = price - min_price
                print(profit)
            else:
                min_price = price
                total_profit = total_profit + profit
                profit = 0
            last_price = price
        total_profit = total_profit + profit
        return total_profit
