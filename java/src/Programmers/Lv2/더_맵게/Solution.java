package Programmers.Lv2.더_맵게;

import java.util.*;

class Solution {
    public int solution(int[] scoville, int K) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (int element: scoville) {
            pq.offer(element);
        }

        int answer = 0;
        while(pq.peek() < K) {
            if (pq.size() == 1) return -1;
            int first = pq.poll();
            int second = pq.poll();
            pq.offer(first + (second) * 2);
            answer++;
        }
        return answer;
    }
}