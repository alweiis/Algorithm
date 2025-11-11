package LeetCode.Easy.LC374_Guess_Number_Higher_or_Lower;

public class Solution extends GuessGame {

    public int guessNumber(int n) {
        int left = 1;
        int right = n;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            int result = guess(mid);
            if (result == 1) {
                left = mid + 1;
            } else if (result == -1) {
                right = mid - 1;
            } else {
                return mid;
            }
        }
        return -1;
    }
}
