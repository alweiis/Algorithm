package LeetCode.Easy.LC232_Implement_Queue_using_Stacks;

import java.util.Stack;

class MyQueue {
    Stack<Integer> stack;
    Stack<Integer> temp;

    public MyQueue() {
        stack = new Stack<>();
        temp = new Stack<>();
    }

    public void push(int x) {
        stack.push(x);
    }

    public int pop() {
        while(stack.size() > 1) {
            temp.push(stack.pop());
        }
        int element = stack.pop();
        while(!temp.isEmpty()) {
            stack.push(temp.pop());
        }
        return element;
    }

    public int peek() {
        while(!stack.isEmpty()) {
            temp.push(stack.pop());
        }
        int peek = temp.peek();
        while(!temp.isEmpty()) {
            stack.push(temp.pop());
        }
        return peek;
    }

    public boolean empty() {
        return stack.isEmpty();
    }
}
