package LeetCode.Medium.LC1318_Minimum_Flips_to_Make_a_OR_b_Equal_to_c;

class Solution {
    public int minFlips(int a, int b, int c) {
        int answer = 0;

        // int는 최대 31비트까지만 확인하면 충분
        for (int i = 0; i < 31; i++) {
            int aBit = (a >> i) & 1;
            int bBit = (b >> i) & 1;
            int cBit = (c >> i) & 1;

            if (cBit == 1) {
                // a | b 가 1이어야 함
                if ((aBit | bBit) == 0) {
                    answer += 1;
                }
            } else {
                // cBit == 0 → a와 b 모두 0이어야 함
                answer += aBit + bBit;
            }
        }

        return answer;
    }
}