package LeetCode.Medium.LC1004_Max_Consecutive_Ones_III;

import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int longestOnes(int[] nums, int k) {
        Queue<Integer> q = new LinkedList<>();
        int output = 0, changed = 0;

        for (int num: nums) {
            if (num == 1) {
                q.offer(num);
            } else {
                if (k == 0) {
                    while(!q.isEmpty()) {
                        q.poll();
                    }
                    continue;
                }
                if (changed == k) {
                    while (!q.isEmpty() && q.peek() == 1) {
                        q.poll();
                    }
                    q.poll();
                    changed--;
                }
                q.offer(num);
                changed++;
            }
            output = Math.max(output, q.size());
        }
        return output;
    }
}
