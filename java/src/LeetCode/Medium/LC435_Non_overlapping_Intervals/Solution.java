package LeetCode.Medium.LC435_Non_overlapping_Intervals;

import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        int endTime = Integer.MIN_VALUE;
        int answer = 0, n = intervals.length;
        Arrays.sort(intervals, (a, b) -> a[1] - b[1]);
        for (int[] interval : intervals) {
            if (endTime <= interval[0]) {
                endTime = interval[1];
            } else {
                answer++;
            }
        }
        return answer;
    }
}