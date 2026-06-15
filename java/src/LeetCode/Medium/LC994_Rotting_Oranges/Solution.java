package LeetCode.Medium.LC994_Rotting_Oranges;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int orangesRotting(int[][] grid) {
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        int m = grid.length;
        int n = grid[0].length;
        int minutes = 0, freshOranges = 0;

        Queue<int[]> queue = new ArrayDeque<>();

        for (int r = 0; r < m; r++) {
            for (int c = 0; c < n; c++) {
                if (grid[r][c] == 1) {
                    freshOranges++;
                } else if (grid[r][c] == 2) {
                    queue.offer(new int[]{r, c});
                }
            }
        }

        if (freshOranges == 0) return 0;

        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean rotted = false;

            for (int i = 0; i < size; i++) {
                int[] current = queue.poll();
                int x = current[0];
                int y = current[1];

                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];

                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                        continue;
                    }

                    if (grid[nx][ny] == 1) {
                        rotted = true;
                        grid[nx][ny] = 2;
                        freshOranges--;
                        queue.offer(new int[]{nx, ny});
                    }
                }
            }
            if (rotted) minutes++;
        }

        if (freshOranges == 0) {
            return minutes;
        } else {
            return -1;
        }
    }
}
