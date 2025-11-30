package LeetCode.Medium.LC1493_Longest_Subarray_of_1s_After_Deleting_One_Element;

class Solution {
    public int longestSubarray(int[] nums) {
        int n = nums.length;
        int l = 0, zeroCount = 0, maxLen = 0;

        for (int r = 0; r < n; r++) {
            if (nums[r] == 0) {
                zeroCount++;
            }
            while (zeroCount > 1) {
                if (nums[l] == 0) {
                    zeroCount--;
                }
                l++;
            }
            maxLen = Math.max(maxLen, r - l);
        }
        return maxLen;
    }
}