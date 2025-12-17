package LeetCode.Easy.LC136_Single_Number;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;

class Solution {
    public int singleNumber(int[] nums) {
        int n = nums.length;
        if (n == 1) return nums[0];

        Arrays.sort(nums);
        Deque<Integer> dq = new ArrayDeque<>();
        for (int num: nums) {
            dq.addLast(num);
        }

        while(dq.size() > 1) {
            int first = dq.pollFirst();
            int second = dq.peekFirst();
            if (first == second) {
                dq.pollFirst();
            } else {
                dq.addLast(first);
            }

        }
        return dq.peek();
    }
}