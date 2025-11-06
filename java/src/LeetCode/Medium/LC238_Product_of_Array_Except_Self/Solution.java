package LeetCode.Medium.LC238_Product_of_Array_Except_Self;

class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] answer = new int[n];
        for (int i = 0; i < n; i++) {
            answer[i] = 1;
        }

        for (int i = 1; i < n; i++) {
            answer[i] *= nums[i-1] * answer[i-1];
        }

        for (int i = n-2; i >= 0; i--) {
            answer[i] *= nums[i+1];
            nums[i] *= nums[i+1];
        }

        return answer;
    }
}
