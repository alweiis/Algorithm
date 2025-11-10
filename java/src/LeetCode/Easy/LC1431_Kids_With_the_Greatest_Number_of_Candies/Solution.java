package LeetCode.Easy.LC1431_Kids_With_the_Greatest_Number_of_Candies;

import java.util.*;

class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int max = Arrays.stream(candies)
                .max()
                .getAsInt();
        List<Boolean> answer = new ArrayList<>();

        for (int i=0; i<candies.length; i++) {
            candies[i] += extraCandies;
            if (candies[i] >= max) {
                answer.add(true);
            } else {
                answer.add(false);
            }
        }

        return answer;
    }
}