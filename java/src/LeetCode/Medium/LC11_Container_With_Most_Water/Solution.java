package LeetCode.Medium.LC11_Container_With_Most_Water;

class Solution {
    public int maxArea(int[] height) {
        int answer = 0;
        int l = 0, r = height.length - 1;
        while (l <=r) {
            if (height[l] < height[r]) {
                answer = Math.max(answer, (r - l) * height[l]);
                l++;
            } else {
                answer = Math.max(answer, (r - l) * height[r]);
                r--;
            }
        }
        return answer;
    }
}