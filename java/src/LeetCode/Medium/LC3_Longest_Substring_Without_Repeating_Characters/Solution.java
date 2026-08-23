package LeetCode.Medium.LC3_Longest_Substring_Without_Repeating_Characters;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int left = 0;
        int maxLength = 0;
        Set<Character> window = new HashSet<>();
        for(int right = 0; right < s.length(); right++){
            char current = s.charAt(right);

            while (window.contains(current)){
                window.remove(s.charAt(left++));
            }

            window.add(current);
            maxLength = Math.max(maxLength, right - left + 1);
        }

        return maxLength;
    }
}
