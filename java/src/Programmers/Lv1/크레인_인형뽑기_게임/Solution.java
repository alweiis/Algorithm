package Programmers.Lv1.크레인_인형뽑기_게임;

import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int count = 0;
        ArrayDeque<Integer> stack = new ArrayDeque<>();
        for (int move : moves) {
            int j = move - 1;
            for (int i = 0; i < board.length; i++) {
                if (board[i][j] != 0) {
                    int num = board[i][j];
                    board[i][j] = 0;
                    if (!stack.isEmpty() && stack.peek() == num) {
                        stack.pop();
                        count += 2;
                    } else {
                        stack.push(num);
                    }
                    break;
                }
            }
        }
        return count;
    }
}