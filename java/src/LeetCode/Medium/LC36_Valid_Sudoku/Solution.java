package LeetCode.Medium.LC36_Valid_Sudoku;

import java.util.*;

class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character> numSet = new HashSet<>();

        for (int i = 0; i < 9; i++) {
            numSet.clear();
            for (int j = 0; j < 9; j++) {
                if (board[i][j] != '.') {
                    if (numSet.contains(board[i][j])) {
                        return false;
                    }
                    numSet.add(board[i][j]);
                }
            }
        }

        for (int j = 0; j < 9; j++) {
            numSet.clear();
            for (int i = 0; i < 9; i++) {
                if (board[i][j] != '.') {
                    if (numSet.contains(board[i][j])) {
                        return false;
                    }
                    numSet.add(board[i][j]);
                }
            }
        }

        for (int i = 0; i <= 6; i += 3) {
            for (int j = 0; j <= 6; j += 3) {
                numSet.clear();
                for (int k = i; k <= i + 2; k++) {
                    for (int l = j; l <= j + 2; l++) {
                        if (board[k][l] != '.') {
                            if (numSet.contains(board[k][l])) {
                                return false;
                            }
                            numSet.add(board[k][l]);
                        }
                    }
                }
            }
        }
        return true;
    }
}