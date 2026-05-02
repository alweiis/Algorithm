package LeetCode.Medium.LC128_Longest_Consecutive_Sequence;

import java.util.*;

class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> numSet = new HashSet<>();
        int maxStreak = 0;
        for(int num: nums) {
            numSet.add(num);
        }

        for (int num: numSet) {
            int current = num;
            if (!numSet.contains(current-1)) {
                int curStreak = 1;
                while (numSet.contains(current+1)) {
                    current++;
                    curStreak++;
                }
                maxStreak = Math.max(maxStreak, curStreak);
            }
        }
        return maxStreak;
    }
}