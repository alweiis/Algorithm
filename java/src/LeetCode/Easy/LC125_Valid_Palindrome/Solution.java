package LeetCode.Easy.LC125_Valid_Palindrome;

class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        StringBuilder sb = new StringBuilder();
        for (char c : s.toCharArray()) {
            if (Character.isLetterOrDigit(c)) {
                sb.append(c);
            }
        }
        String origin = sb.toString();
        String reversed = sb.reverse().toString();
        return origin.equals(reversed);
    }
}