package LeetCode.Easy.LC933_Number_of_Recent_Calls;

import java.util.LinkedList;
import java.util.Queue;

class RecentCounter {
    Queue<Integer> que = new LinkedList<>();
    int count;

    public RecentCounter() {
        count = 0;
    }

    public int ping(int t) {
        count = 1;

        int min = t - 3000;
        int max = t;
        int size = que.size();

        for(int i = 0; i < size; i++) {
            int number = que.poll();
            if (number >= min && number <= max) {
                count++;
                que.offer(number);
            }
        }
        que.offer(t);

        return count;
    }
}