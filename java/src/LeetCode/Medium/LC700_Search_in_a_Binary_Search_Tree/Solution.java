package LeetCode.Medium.LC700_Search_in_a_Binary_Search_Tree;

class Solution {
    public TreeNode searchBST(TreeNode root, int val) {
        while (true) {
            if (root.val == val) return root;

            if (root.val > val) {
                if (root.left == null) return null;
                root = root.left;
            } else {
                if (root.right == null) return null;
                root = root.right;
            }
        }
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