package LeetCode.Easy.LC217_Contains_Duplicate;

import java.util.HashSet;
import java.util.Set;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (!seen.add(num)) { // 이미 있으면 false 반환
                return true;
            }
        }
        return false;
    }
}

