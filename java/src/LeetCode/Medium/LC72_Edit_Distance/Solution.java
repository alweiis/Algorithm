package LeetCode.Medium.LC72_Edit_Distance;

class Solution {
    public int minDistance(String word1, String word2) {
        int m = word1.length(), n = word2.length();
        if (n == 0 || m == 0)       return Math.max(n, m);
        if (word1.equals(word2))    return 0;

        int[][] dp = new int[m+1][n+1];

        for (int i = 1; i <= m; i++) dp[i][0] = i;
        for (int j = 1; j <= n; j++) dp[0][j] = j;

        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                if (word1.charAt(i-1) == word2.charAt(j-1)) {
                    dp[i][j] = dp[i-1][j-1];
                } else {
                    int delete = dp[i-1][j] + 1;      // 삭제
                    int insert = dp[i][j-1] + 1;      // 삽입
                    int replace = dp[i-1][j-1] + 1;   // 교체
                    dp[i][j] = Math.min(delete, Math.min(insert, replace));
                }
            }
        }

        return dp[m][n];
    }
}