package LeetCode.Easy.LC1732_Find_the_Highest_Altitude;

public class Solution {
    public int largestAltitude(int[] gain) {
        int n = gain.length;
        int[] prefix = new int[n+1];
        int highest = prefix[0];

        for (int i = 0; i < n; i++) {
            prefix[i+1] = gain[i] + prefix[i];
            highest = Math.max(highest, prefix[i+1]);
        }
        return highest;
    }
}
