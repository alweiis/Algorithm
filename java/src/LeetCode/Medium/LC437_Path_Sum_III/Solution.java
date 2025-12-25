package LeetCode.Medium.LC437_Path_Sum_III;

class Solution {
    int output = 0;

    public int pathSum(TreeNode root, int targetSum) {
        if (root == null) return 0;

        dfs(root, targetSum);

        pathSum(root.left, targetSum);
        pathSum(root.right, targetSum);

        return output;
    }

    private void dfs(TreeNode node, long remaining) {
        if (node == null) return;

        if (node.val == remaining) {
            output++;
        }

        dfs(node.left, remaining - node.val);
        dfs(node.right, remaining - node.val);
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