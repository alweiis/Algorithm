package LeetCode.Easy.LC338_Counting_Bits;

class Solution {
    public int[] countBits(int n) {
        int[] ans = new int[n+1];
        for (int i = 0; i <= n; i++) {
            String str = Integer.toString(i, 2);
            int count = (int) str.chars().filter(c -> c == '1').count();
            ans[i] = count;
        }
        return ans;
    }
}