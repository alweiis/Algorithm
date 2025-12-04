package LeetCode.Medium.LC875_Koko_Eating_Bananas;

class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        int k = Integer.MAX_VALUE, l = 1, r = 1000000000;
        while (l <= r) {
            int m = l + (r - l) / 2;
            long hour = 0;
            for (int pile : piles) {
                if (pile % m == 0) {
                    hour += pile / m;
                } else {
                    hour += (pile / m) + 1;
                }
            }
            if (hour <= h) {
                r = m - 1;
                k = Math.min(k, m);
            } else {
                l = m + 1;
            }
        }
        return k;
    }
}