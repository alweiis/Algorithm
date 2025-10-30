package LeetCode.Easy.LC643_Maximum_Average_Subarray_I;

public class Solution {
    public double findMaxAverage(int[] nums, int k) {
        double sum = 0;
        int n = nums.length;

        for (int i = 0; i < k; i++) {
            sum += nums[i];
        }
        double average = sum / k;
        for (int i = k; i < n; i++) {
            sum += (nums[i] - nums[i-k]);
            average = Math.max(average, sum / k);
        }
        return average;
    }
}