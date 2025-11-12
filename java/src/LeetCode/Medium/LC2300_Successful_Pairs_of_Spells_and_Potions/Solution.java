package LeetCode.Medium.LC2300_Successful_Pairs_of_Spells_and_Potions;

import java.util.Arrays;

class Solution {
    public int[] successfulPairs(int[] spells, int[] potions, long success) {
        int n = spells.length;
        int m = potions.length;
        int[] result = new int[n];

        Arrays.sort(potions);
        for (int i = 0; i < n; i++) {
            long spell = spells[i];
            int idx = lowerBound(potions, spell, success);
            result[i] = m - idx;
        }
        return result;
    }

    private int lowerBound(int[] potions, long spell, long success) {
        int left = 0, right = potions.length - 1;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long product = spell * potions[mid];

            if (product >= success) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
}