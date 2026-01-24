package LeetCode.Easy.LC141_Linked_List_Cycle;

public class Solution {
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;

        ListNode current = head;

        while (current.next != null) {
            if (current.val == 100001) return true;
            current.val = 100001;
            current = current.next;
        }
        return false;
    }
}

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) {
        val = x;
        next = null;
    }
}