package Programmers.Lv3.네트워크;

import java.util.*;

class Solution {
    boolean[] visited;
    int[][] computers;

    public int solution(int n, int[][] computers) {
        int answer = 0;
        visited = new boolean[n];
        this.computers = computers;

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                answer++;
                bfs(i);
            }
        }
        return answer;
    }

    private void bfs(int i) {
        ArrayDeque<Integer> queue = new ArrayDeque<>();
        queue.add(i);
        visited[i] = true;
        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int j = 0; j < computers.length; j++) {
                if (!visited[j] && computers[curr][j] == 1) {
                    queue.add(j);
                    visited[j] = true;
                }
            }
        }
    }

    private void dfs(int curr) {
        visited[curr] = true;
        for (int j = 0; j < computers.length; j++) {
            if (!visited[j] && computers[curr][j] == 1) {
                dfs(j);
            }
        }
    }
}