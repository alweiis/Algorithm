package LeetCode.Medium.LC1456_Maximum_Number_of_Vowels_in_a_Substring_of_Given_Length;

class Solution {
    public int maxVowels(String s, int k) {
        char[] arr = s.toCharArray();
        int maxNum = 0, tempNum = 0;
        for (int i = 0; i < k; i++) {
            if (isVowel(arr[i])) maxNum++;
        }
        tempNum = maxNum;

        for (int i = k; i < s.length(); i++) {
            if (isVowel(arr[i])) tempNum++;
            if (isVowel(arr[i-k])) tempNum--;
            if (tempNum > maxNum)  maxNum = tempNum;
        }
        return maxNum;
    }

    private boolean isVowel(char c) {
        return "aeiou".indexOf(c) >= 0;
    }
}