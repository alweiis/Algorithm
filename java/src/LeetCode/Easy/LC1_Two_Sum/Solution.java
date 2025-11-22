package LeetCode.Easy.LC1_Two_Sum;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2];
        int n = nums.length;

        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            map.put(nums[i], i);
        }

        int key = 0;
        for (int i = 0; i < n; i++) {
            key = target - nums[i];
            if (map.containsKey(key) && map.get(key) != i) {
                answer[0] = i;
                answer[1] = map.get(key);
                break;
            }
        }
        return answer;
    }
}
