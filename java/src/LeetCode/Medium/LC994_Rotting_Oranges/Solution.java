package LeetCode.Medium.LC994_Rotting_Oranges;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int orangesRotting(int[][] grid) {
        int m = grid.length;
        int n = grid[0].length;

        int[][] directions = {
                {-1, 0}, // up
                {1, 0},  // down
                {0, -1}, // left
                {0, 1}   // right
        };

        Queue<int[]> queue = new ArrayDeque<>();
        // 초기 썩은 오렌지 큐에 추가
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if(grid[r][c] == 2) {
                    queue.offer(new int[]{r, c});
                }
            }
        }

        int minute = 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean rotted = false;

            for (int i = 0; i < size; i++) {
                int[] cur = queue.poll();
                int r = cur[0];
                int c = cur[1];

                for (int[] dir: directions) {
                    int nr = r + dir[0];
                    int nc = c + dir[1];

                    if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
                    if (grid[nr][nc] != 1) continue;

                    grid[nr][nc] = 2;
                    queue.offer(new int[]{nr, nc});
                    rotted = true;
                }
            }
            if (rotted) minute++;
        }

        // 아직 안 썩은 오렌지가 있는지 확인
        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if(grid[r][c] == 1) return -1;
            }
        }
        return minute;
    }
}
