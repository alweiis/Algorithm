package LeetCode.Medium.LC151_Reverse_Words_in_a_String;

public class Solution {
    public String reverseWords(String s) {
        String[] strings = s.trim().replaceAll("\\s+", " ").split(" ");
        StringBuilder sb = new StringBuilder();
        for (int i = strings.length - 1; i >= 0; i--) {
            sb.append(strings[i]);
            if (i != 0) sb.append(" ");
        }
        return sb.toString();
    }
}
