package LeetCode.Medium.LC1004_Max_Consecutive_Ones_III;

import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int longestOnes(int[] nums, int k) {
        Deque<Integer> q = new ArrayDeque<>();
        int maxLen = 0, zeroCount = 0;

        for (int num: nums) {
            if (num == 1) {
                q.addLast(num);
            } else {
                if (k == 0) {
                    q.clear();
                    continue;
                }
                if (zeroCount == k) {
                    while (!q.isEmpty() && q.peek() == 1) {
                        q.pollFirst();
                    }
                    q.pollFirst();
                    zeroCount--;
                }
                q.addLast(num);
                zeroCount++;
            }
            maxLen = Math.max(maxLen, q.size());
        }
        return maxLen;
    }
}
