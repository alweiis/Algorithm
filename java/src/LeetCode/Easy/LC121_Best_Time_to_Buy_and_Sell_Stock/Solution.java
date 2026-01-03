package LeetCode.Easy.LC121_Best_Time_to_Buy_and_Sell_Stock;

class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0];
        int maxProfit = 0;
        for (int price : prices) {
            if (price < minPrice) minPrice = price;
            maxProfit = Math.max(maxProfit, price - minPrice);
        }
        return maxProfit;
    }
}
