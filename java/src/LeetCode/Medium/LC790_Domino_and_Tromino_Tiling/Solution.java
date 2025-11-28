package LeetCode.Medium.LC790_Domino_and_Tromino_Tiling;

class Solution {
    public int numTilings(int n) {
        final long MOD = 1_000_000_007L;
        if (n == 0) return 1;
        if (n == 1) return 1;
        if (n == 2) return 2;

        long f0 = 1; // f[0]
        long f1 = 1; // f[1]
        long f2 = 2; // f[2]
        long fi = 0;

        for (int i = 3; i <= n; i++) {
            fi = (2 * f2 + f0) % MOD; // f[i] = 2*f[i-1] + f[i-3]
            // shift
            f0 = f1;
            f1 = f2;
            f2 = fi;
        }
        return (int) fi;
    }
}