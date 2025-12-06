package LeetCode.Medium.LC2130_Maximum_Twin_Sum_of_a_Linked_List;

import java.util.ArrayList;
import java.util.List;

class Solution {
    public int pairSum(ListNode head) {
        List<Integer> arrayList = new ArrayList<>();
        int max = 0;
        ListNode curr = head;
        while (curr != null) {
            arrayList.add(curr.val);
            curr = curr.next;
        }
        int n = arrayList.size();
        for (int i = 0; i < n / 2; i++) {
            int temp = arrayList.get(i) + arrayList.get(n - i - 1);
            max = Math.max(max, temp);
        }

        return max;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}