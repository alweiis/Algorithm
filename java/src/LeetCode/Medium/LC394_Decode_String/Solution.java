package LeetCode.Medium.LC394_Decode_String;

import java.util.Stack;
import java.util.Stack;

class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        for (char c : s.toCharArray()) {
            if (c == ']') {
                // 1) 괄호 안 문자열을 뒤에서부터 뽑아 옳은 순서로 만든다
                StringBuilder sb = new StringBuilder();
                while (!stack.isEmpty() && stack.peek() != '[') {
                    sb.insert(0, stack.pop()); // 앞에 붙여서 원래 순서 유지
                }

                // 2) '[' 제거
                if (!stack.isEmpty() && stack.peek() == '[') {
                    stack.pop();
                }

                // 3) 숫자(반복 횟수) 추출 (다자리 수 처리)
                StringBuilder nb = new StringBuilder();
                while (!stack.isEmpty() && Character.isDigit(stack.peek())) {
                    nb.insert(0, stack.pop()); // 앞에 붙여서 정상 순서로 만든다
                }
                int k = 1;
                if (!nb.isEmpty()) {
                    k = Integer.parseInt(nb.toString());
                }

                // 4) sb를 k번 스택에 다시 push
                String segment = sb.toString();
                for (int i = 0; i < k; i++) {
                    for (char ch : segment.toCharArray()) {
                        stack.push(ch);
                    }
                }
            } else {
                // '[' 도 스택에 넣어야 경계를 알 수 있다
                stack.push(c);
            }
        }

        // 스택의 내용을 문자열로 조합
        StringBuilder result = new StringBuilder();
        for (char ch : stack) result.append(ch);
        return result.toString();
    }
}