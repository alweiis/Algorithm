package LeetCode.Easy.LC1768_Merge_Strings_Alternately;

public class Solution {
    public String mergeAlternately(String word1, String word2) {
        int l1 = word1.length(), l2 = word2.length();
        int idx1 = 0, idx2 = 0;
        StringBuilder sb = new StringBuilder();

        while (true) {
            if (idx1 == l1 || idx2 == l2) {
                break;
            }
            sb.append(word1.charAt(idx1++));
            sb.append(word2.charAt(idx2++));
        }

        while (idx1 < l1) {
            sb.append(word1.charAt(idx1++));
        }
        while (idx2 < l2) {
            sb.append(word2.charAt(idx2++));
        }

        return sb.toString();
    }
}