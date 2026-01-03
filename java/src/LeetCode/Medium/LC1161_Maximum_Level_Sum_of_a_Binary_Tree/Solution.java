package LeetCode.Medium.LC1161_Maximum_Level_Sum_of_a_Binary_Tree;

import java.util.ArrayDeque;
import java.util.Queue;

class Solution {

    public int maxLevelSum(TreeNode root) {
        Queue<TreeNode> queue = new ArrayDeque<>();
        queue.offer(root);

        int currentLevel = 1;
        int answerLevel = 1;
        long maxSum = Long.MIN_VALUE;

        while (!queue.isEmpty()) {
            int levelSize = queue.size();
            long levelSum = 0;

            // 현재 레벨의 모든 노드 처리
            for (int i = 0; i < levelSize; i++) {
                TreeNode node = queue.poll();
                levelSum += node.val;

                if (node.left != null) {
                    queue.offer(node.left);
                }
                if (node.right != null) {
                    queue.offer(node.right);
                }
            }

            // 레벨 단위 후처리
            if (levelSum > maxSum) {
                maxSum = levelSum;
                answerLevel = currentLevel;
            }
            currentLevel++;
        }
        return answerLevel;
    }
}


class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) {
        this.val = val;
    }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
