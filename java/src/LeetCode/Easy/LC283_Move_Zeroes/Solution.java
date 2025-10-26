package LeetCode.Easy.LC283_Move_Zeroes;

public class Solution {
    public void moveZeroes(int[] nums) {
        int lt = 0, n = nums.length;

        for (int rt = 0; rt < n; rt++) {
            if (nums[lt] == 0 && nums[rt] != 0) {
                int temp = nums[rt];
                nums[rt] = nums[lt];
                nums[lt] = temp;

                lt++;
            }
            if (nums[lt] != 0) {
                lt++;
            }
        }
    }
}