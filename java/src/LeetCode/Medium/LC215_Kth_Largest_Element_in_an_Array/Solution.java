package LeetCode.Medium.LC215_Kth_Largest_Element_in_an_Array;

import java.util.Collections;
import java.util.PriorityQueue;

class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        for (int num: nums) {
            maxHeap.offer(num);
        }

        int count = 0, answer = 0;
        while(!maxHeap.isEmpty()) {
            answer = maxHeap.poll();
            count++;
            if (count == k) break;
        }
        return answer;
    }
}