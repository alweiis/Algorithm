package LeetCode.Easy.LC228_Summary_Ranges;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> answer = new ArrayList<>();
        int length = nums.length;
        int start = 0, end = 0;

        for (int i = 1; i < length; i++) {
            if (nums[i] == (long) nums[end] + 1) {
                end = i;
            } else {
                if (start == end) {
                    answer.add(String.valueOf(nums[start]));
                } else {
                    answer.add(nums[start] + "->" + nums[end]);
                }
                end = i;
                start = i;
            }
        }
        if (length >= 1) {
            if (start == end) {
                answer.add(String.valueOf(nums[start]));
            } else {
                answer.add(nums[start] + "->" + nums[end]);
            }
        }
        return answer;
    }
}