package LeetCode.Medium.LC200_Number_of_Islands;

import java.util.*;

class Solution {
    int m, n;
    int[] dx = {0, 1, 0, -1};
    int[] dy = {1, 0, -1, 0};

    public int numIslands(char[][] grid) {
        m = grid.length;
        n = grid[0].length;
        int answer = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    answer++;
                    bfs(i, j, grid);
                }
            }
        }
        return answer;
    }

    private void bfs(int i, int j, char[][] grid) {
        Queue<int[]> queue = new ArrayDeque<>();
        queue.offer(new int[] {i, j});
        grid[i][j] = '0';

        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k];
                int ny = y + dy[k];

                if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;
                if (grid[nx][ny] == '0') continue;

                queue.offer(new int[] {nx, ny});
                grid[nx][ny] = '0';
            }
        }
    }
}