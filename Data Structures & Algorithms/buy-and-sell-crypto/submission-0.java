class Solution {
    public int maxProfit(int[] prices) {
       int buy = 0;
       int sell = 1;
       int currentProfit = 0;
       int maxProfit = 0;
       
       while(sell < prices.length) {
            if(prices[sell] > prices[buy] ) {
                currentProfit = prices[sell] - prices[buy];
                if(currentProfit > maxProfit) {
                    maxProfit = currentProfit;
                }
            }

            if(prices[sell] < prices[buy]) {
                buy = sell;
            }
            sell++;
       }
       return maxProfit;
    }
}
