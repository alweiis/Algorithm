package LeetCode.Easy.LC14_Longest_Common_Prefix;

import java.util.Arrays;

class Solution {
    public String longestCommonPrefix(String[] strs) {
        Arrays.sort(strs);
        int length = strs[0].length();
        if (length == 0) return "";

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < length; i++) {
            for (int j = 1; j < strs.length; j++) {
                if (strs[j-1].charAt(i) != strs[j].charAt(i)) {
                    return sb.toString();
                }
            }
            sb.append(strs[0].charAt(i));
        }
        return sb.toString();
    }
}