package LeetCode.Medium.LC1372_Longest_ZigZag_Path_in_a_Binary_Tree;

class Solution {
    int count = 0;

    public int longestZigZag(TreeNode root) {
        dfsRight(root.right, 1);
        dfsLeft(root.left, 1);
        return count;
    }

    private void dfsRight(TreeNode node, int currentCount) {
        if (node == null) {
            return;
        }
        count = Math.max(count, currentCount);
        dfsLeft(node.left, currentCount + 1);
        dfsRight(node.right, 1);
    }

    private void dfsLeft(TreeNode node, int currentCount) {
        if (node == null) {
            return;
        }
        count = Math.max(count, currentCount);
        dfsRight(node.right, currentCount + 1);
        dfsLeft(node.left, 1);
    }
}

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}