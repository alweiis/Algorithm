package LeetCode.Medium.LC36_Valid_Sudoku;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        boolean[][] rows = new boolean[9][9];
        boolean[][] cols = new boolean[9][9];
        boolean[][] boxes = new boolean[9][9];

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    int n = board[i][j] - '0' - 1;
                    int boxIndex = (i / 3) * 3 + (j / 3);

                    if (rows[i][n]) {
                        return false;
                    }
                    rows[i][n] = true;

                    if (cols[j][n]) {
                        return false;
                    }
                    cols[j][n] = true;

                    if (boxes[boxIndex][n]) {
                        return false;
                    }
                    boxes[boxIndex][n] = true;
                }
            }
        }
        return true;
    }
}