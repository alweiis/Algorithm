package LeetCode.Easy.LC605_Can_Place_Flowers;

class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int L = flowerbed.length;
        for (int i = 0; i < L; i++) {
            if (flowerbed[i] == 0) {
                if (i == 0) {
                    if (L == 1) {
                        flowerbed[i] = 1;
                        n--;
                    } else if (flowerbed[i + 1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
                if (i > 0 && i < L-1) {
                    if (flowerbed[i-1] == 0 && flowerbed[i+1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
                if (i == L-1) {
                    if (L > 1 && flowerbed[i-1] == 0) {
                        flowerbed[i] = 1;
                        n--;
                    }
                }
            }

            if (n <= 0) {
                return true;
            }
        }
        return false;
    }
}
