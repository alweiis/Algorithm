package LeetCode.Medium.LC1372_Longest_ZigZag_Path_in_a_Binary_Tree;

class Solution {
    int count = 0;

    public int longestZigZag(TreeNode root) {
        dfsRight(root.right, 0);
        dfsLeft(root.left, 0);

        return count;
    }

    private void dfsRight(TreeNode node, int currentCount) {
        if (node == null) {
            count = Math.max(count, currentCount);
            return;
        }
        dfsLeft(node.left, currentCount + 1);
        dfsRight(node.right, 0);
    }

    private void dfsLeft(TreeNode node, int currentCount) {
        if (node == null) {
            count = Math.max(count, currentCount);
            return;
        }
        dfsRight(node.right, currentCount + 1);
        dfsLeft(node.left, 0);
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