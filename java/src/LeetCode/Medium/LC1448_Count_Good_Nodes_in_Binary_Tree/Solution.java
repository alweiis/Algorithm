package LeetCode.Medium.LC1448_Count_Good_Nodes_in_Binary_Tree;

class Solution {
    int goodNode = 0;

    public int goodNodes(TreeNode root) {
        dfs(root, Integer.MIN_VALUE);
        return goodNode;
    }

    private void dfs(TreeNode root, int max) {
        if (root == null) return;

        if (root.val >= max) {
            goodNode++;
            max = root.val;
        }
        dfs(root.left, max);
        dfs(root.right, max);
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