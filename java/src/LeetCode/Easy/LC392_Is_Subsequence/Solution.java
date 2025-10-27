package LeetCode.Easy.LC392_Is_Subsequence;

public class Solution {
    public boolean isSubsequence(String s, String t) {
        int length1 = s.length(), length2 = t.length();
        int p1 = 0;

        if (length1 == 0) {
            return true;
        }

        for (int p2 = 0; p2 < length2; p2++) {
            if (p1 < length1 && s.charAt(p1) == t.charAt(p2)) {
                p1++;
            }
        }
        return p1 == length1;
    }
}
