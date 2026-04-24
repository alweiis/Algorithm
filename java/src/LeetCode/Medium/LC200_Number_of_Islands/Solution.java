package LeetCode.Medium.LC200_Number_of_Islands;

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
                    dfs(i, j, grid);
                }
            }
        }
        return answer;
    }

    private void dfs(int x, int y, char[][] grid) {
        if (x < 0 || x >= m || y < 0 || y >= n || grid[x][y] == '0') {
            return;
        }
        grid[x][y] = '0';

        for (int k = 0; k < 4; k++) {
            dfs(x + dx[k], y + dy[k], grid);
        }
    }
}