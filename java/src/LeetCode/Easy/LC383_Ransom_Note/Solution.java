package LeetCode.Easy.LC383_Ransom_Note;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        int[] alphabets = new int[26];

        for (char c: magazine.toCharArray()) {
            alphabets[c -'a']++;
        }

        for (char c: ransomNote.toCharArray()) {
            if (alphabets[c -'a'] < 1) {
                return false;
            }
            alphabets[c -'a']--;
        }
        return true;
    }
}