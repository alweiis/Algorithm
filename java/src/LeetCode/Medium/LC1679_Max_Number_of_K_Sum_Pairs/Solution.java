package LeetCode.Medium.LC1679_Max_Number_of_K_Sum_Pairs;

import java.util.Arrays;

class Solution {
    public int maxOperations(int[] nums, int k) {
        Arrays.sort(nums);
        int l = 0, r = nums.length - 1, ops = 0;
        while (l < r) {
            int sum = nums[l] + nums[r];
            if (sum == k) {
                ops++;
                l++;
                r--;
            } else if (sum < k) {
                l++;
            } else {
                r--;
            }
        }
        return ops;
    }
}
