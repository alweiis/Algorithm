package LeetCode.Medium.LC1162_As_Far_from_Land_as_Possible;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int maxDistance(int[][] grid) {
        int[] dx = {0, 0, 1, -1};
        int[] dy = {1, -1, 0, 0};

        int m = grid.length;
        int n = grid[0].length;

        Queue<int[]> queue = new ArrayDeque<>();
        for (int x = 0; x < m; x++) {
            for (int y = 0; y < n; y++) {
                if (grid[x][y] == 1) {
                    queue.offer(new int[]{x, y});
                }
            }
        }
        if (queue.isEmpty() || queue.size() == m * n) {
            return -1;
        }

        int distance = 0;
        while(!queue.isEmpty()) {
            int size = queue.size();

            for (int i = 0; i < size; i++) {
                int[] current = queue.poll();
                int x = current[0];
                int y = current[1];

                for (int k = 0; k < 4; k++) {
                    int nx = x + dx[k];
                    int ny = y + dy[k];

                    if (nx < 0 || nx >= m || ny < 0 || ny >= n) continue;

                    if (grid[nx][ny] == 0) {
                        queue.offer(new int[]{nx, ny});
                        grid[nx][ny] = 1;
                    }
                }
            }

            distance++;
        }

        return distance - 1;
    }
}