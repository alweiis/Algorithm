package LeetCode.Medium.LC901_Online_Stock_Span;

import java.util.Stack;

class StockSpanner {
    private Stack<int[]> stack;

    public StockSpanner() {
        stack = new Stack<>();
    }

    public int next(int price) {
        int span = 1;   // 오늘은 항상 포함

        // 현재 가격보다 작거나 같은 가격 제거
        while (!stack.isEmpty() && stack.peek()[0] <= price)  {
            span += stack.pop()[1];
        }

        // 현재 가격과 계산된 스팬 저장
        stack.push(new int[]{price, span});

        return span;
    }
}