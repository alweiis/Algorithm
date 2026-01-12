package LeetCode.Medium.LC452_Minimum_Number_of_Arrows_to_Burst_Balloons;

import java.util.Arrays;

class Solution {
    public int findMinArrowShots(int[][] points) {
        Arrays.sort(points, (a, b) -> Integer.compare(a[1], b[1]));

        int arrows = 1;
        int arrowPos = points[0][1];

        for (int[] point: points) {
            if (point[0] > arrowPos) {
                arrows++;
                arrowPos = point[1];
            }
        }
        return arrows;
    }
}