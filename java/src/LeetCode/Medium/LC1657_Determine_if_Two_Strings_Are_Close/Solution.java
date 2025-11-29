package LeetCode.Medium.LC1657_Determine_if_Two_Strings_Are_Close;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean closeStrings(String word1, String word2) {
        int n1 = word1.length();
        int n2 = word2.length();
        if (n1 != n2) return false;

        Map<Character, Integer> map1 = new HashMap<>();
        Map<Character, Integer> map2 = new HashMap<>();

        for(char c: word1.toCharArray()) {
            map1.put(c, map1.getOrDefault(c, 0) + 1);
        }

        for(char c: word2.toCharArray()) {
            map2.put(c, map2.getOrDefault(c, 0) + 1);
        }

        int[] arr1 = new int[n1];
        int[] arr2 = new int[n2];
        int idx1 = 0, idx2 = 0;
        for (Character key: map2.keySet()) {
            int num = map1.getOrDefault(key, 0);
            if (num == 0) return false;
            arr1[idx1++] = num;
        }

        for (Character key: map1.keySet()) {
            int num = map2.getOrDefault(key, 0);
            if (num == 0) return false;
            arr2[idx2++] = num;
        }

        Arrays.sort(arr1);
        Arrays.sort(arr2);
        return Arrays.equals(arr1, arr2);
    }
}