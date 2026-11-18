class  Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        pre_min=prices[0]
        index_of_pre_min = 0
        price_min  = prices[0]
        index_of_min = 0
        price_max = prices[0]
        index_of_max=0

        for i in range(1, len(prices)):
             if price_max < prices[i] or prices[i] - price_min > price_max - pre_min:
                 price_max = prices[i]
                 index_of_max = i

             if prices[i] < price_min:
                 price_min = prices[i]
                 index_of_min = i
             
             if index_of_min < index_of_max:
                 pre_min = price_min
                 index_of_pre_min = index_of_min


        if  index_of_max > index_of_pre_min:
             return  price_max - pre_min
        
        return  0
