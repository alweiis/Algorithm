package LeetCode.Medium.LC714_Best_Time_to_Buy_and_Sell_Stock_with_Transaction_Fee;

class Solution {
    public int maxProfit(int[] prices, int fee) {
        int cash = 0, hold = - prices[0], n = prices.length;

        for (int i = 1; i < n; i++) {
            cash = Math.max(cash, hold + prices[i] - fee);
            hold = Math.max(hold, cash - prices[i]);
        }
        return cash;
    }
}