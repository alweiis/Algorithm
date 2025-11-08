package LeetCode.Medium.LC735_Asteroid_Collision;

import java.util.Stack;

class Solution {
    public int[] asteroidCollision(int[] asteroids) {
        Stack<Integer> stack = new Stack<>();
        for (int curr: asteroids) {
            if (stack.isEmpty()) {
                stack.push(curr);
            } else {
                boolean addable = true;
                while (!stack.isEmpty()) {
                    int top = stack.peek();
                    if (top > 0 && curr < 0) {
                        int absTop = Math.abs(top);
                        int absCur = Math.abs(curr);
                        if (absTop == absCur) {
                            stack.pop();
                            addable = false;
                            break;
                        } else if (absTop < absCur) {
                            stack.pop();
                        } else {
                            addable = false;
                            break;
                        }
                    } else {
                        stack.push(curr);
                        addable = false;
                        break;
                    }
                }
                if (addable) {
                    stack.push(curr);
                }
            }
        }

        return stack.stream().mapToInt(Integer::intValue).toArray();
    }
}