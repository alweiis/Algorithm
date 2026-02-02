package LeetCode.Medium.LC1926_Nearest_Exit_from_Entrance_in_Maze;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public int nearestExit(char[][] maze, int[] entrance) {
        int m = maze.length;
        int n = maze[0].length;

        int startRow = entrance[0];
        int startCol = entrance[1];

        int[][] directions = {
                {-1, 0}, // up
                {1, 0},  // down
                {0, -1}, // left
                {0, 1}   // right
        };

        Queue<int[]> queue = new ArrayDeque<>();
        boolean[][] visited = new boolean[m][n];

        // row, col, steps
        queue.offer(new int[]{startRow, startCol, 0});
        visited[startRow][startCol] = true;

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int row = cur[0];
            int col = cur[1];
            int steps = cur[2];

            for (int[] dir : directions) {
                int nr = row + dir[0];
                int nc = col + dir[1];

                // 범위 체크
                if (nr < 0 || nr >= m || nc < 0 || nc >= n) {
                    continue;
                }

                // 이동 가능 여부 체크
                if (maze[nr][nc] != '.' || visited[nr][nc]) {
                    continue;
                }

                // 출구 여부 체크 (entrance 제외는 이미 보장됨)
                if (nr == 0 || nr == m - 1 || nc == 0 || nc == n - 1) {
                    return steps + 1;
                }

                visited[nr][nc] = true;
                queue.offer(new int[]{nr, nc, steps + 1});
            }
        }
        return -1;
    }
}
