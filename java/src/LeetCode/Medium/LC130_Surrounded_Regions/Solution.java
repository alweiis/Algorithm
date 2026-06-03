package LeetCode.Medium.LC130_Surrounded_Regions;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {
    public void solve(char[][] board) {
        int[] dx = {1, 0, 0, -1};
        int[] dy = {0, 1, -1, 0};

        int m = board.length;
        int n = board[0].length;

        Queue<int[]> queue = new ArrayDeque<>();

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 || i == m-1 || j == 0 || j == n-1) {
                    if (board[i][j] == 'O') {
                        queue.offer(new int[]{i, j});
                        board[i][j] = 'S';
                    }
                }
            }
        }

        while(!queue.isEmpty()) {
            int[] current = queue.poll();
            int x = current[0];
            int y = current[1];

            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d];
                int ny = y + dy[d];

                if (nx < 0 || nx >= m || ny < 0 || ny >= n) {
                    continue;
                }

                if (board[nx][ny] == 'O') {
                    queue.offer(new int[]{nx, ny});
                    board[nx][ny] = 'S';
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O') {
                    board[i][j] = 'X';
                } else if (board[i][j] == 'S') {
                    board[i][j] = 'O';
                }
            }
        }
    }
}