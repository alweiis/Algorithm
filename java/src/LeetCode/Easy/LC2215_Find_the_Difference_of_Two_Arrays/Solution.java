package LeetCode.Easy.LC2215_Find_the_Difference_of_Two_Arrays;

import java.util.*;
public class Solution {
    public List<List<Integer>> findDifference(int[] nums1, int[] nums2) {
        List<List<Integer>> answer = new ArrayList<>();
        List<Integer> list1 = new ArrayList<>();
        List<Integer> list2 = new ArrayList<>();

        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();

        for (int number: nums1) {
            set1.add(number);
        }

        for (int number: nums2) {
            set2.add(number);
        }

        for (Integer num: set1) {
            if (!set2.contains(num)) {
                list1.add(num);
            }
        }

        for (Integer num: set2) {
            if (!set1.contains(num)) {
                list2.add(num);
            }
        }

        answer.add(list1);
        answer.add(list2);

        return answer;
    }
}