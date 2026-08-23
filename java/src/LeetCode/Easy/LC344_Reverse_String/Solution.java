package LeetCode.Easy.LC344_Reverse_String;

class Solution {
    public void reverseString(char[] s) {
        int length = s.length;
        char tmp = ' ';

        for (int i = 0; i < length / 2; i++) {
            tmp = s[i];
            s[i] = s[length - 1 - i];
            s[length - 1 - i] = tmp;
        }
    }
}