package LeetCode.Medium.LC162_Find_Peak_Element;

class Solution {
    public int findPeakElement(int[] nums) {
        int n = nums.length;
        if (n == 1) return 0;

        int left = 0, right = n - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (mid == 0) {
                if (nums[0] > nums[1]) return 0;
                left = mid + 1;
            } else if (mid == n - 1) {
                if (nums[n - 1] > nums[n - 2]) return n - 1;
                right = mid - 1; // 원래 코드의 l = m - 1 은 버그
            } else {
                if (nums[mid - 1] < nums[mid] && nums[mid + 1] < nums[mid]) {
                    return mid;
                } else if (nums[mid] < nums[mid + 1]) {
                    left = mid + 1;
                } else {
                    right = mid - 1;
                }
            }
        }
        return -1; // 이론상 도달하지 않음 (문제 조건 상 항상 peak 존재)
    }
}