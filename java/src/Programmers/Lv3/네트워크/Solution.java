package Programmers.Lv3.네트워크;

import java.util.*;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        boolean[] visited = new boolean[n];
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                bfs(n, computers, i, visited);
            }
        }
        return answer;
    }

    private void bfs(int n, int[][] computers, int i, boolean[] visited) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(i);
        visited[i] = true;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int j = 0; j < n; j++) {
                if (!visited[j] && computers[curr][j] == 1) {
                    queue.add(j);
                    visited[j] = true;
                }
            }
        }
    }
}