package Programmers.Lv2.기능개발;

import java.util.*;

public class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        List<Integer> answerList = new ArrayList<>();

        // 1. 첫 번째 기능이 배포되기까지 남은 일수 계산
        int maxDay = (int) Math.ceil((100.0 - progresses[0]) / speeds[0]);
        int count = 1; // 배포될 기능의 수

        // 2. 두 번째 기능부터 순회하며 비교
        for (int i = 1; i < progresses.length; i++) {
            // 현재 기능의 남은 일수 계산
            int days = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);

            if (days <= maxDay) {
                // 앞의 기능이 끝날 때까지 기다려야 하므로 함께 배포
                count++;
            } else {
                // 앞의 기능들보다 늦게 끝나므로, 이전까지 쌓인 기능들을 먼저 배포
                answerList.add(count);
                count = 1;     // 카운트 초기화
                maxDay = days; // 기준일을 현재 기능의 완성일로 갱신
            }
        }

        // 3. 마지막으로 쌓여있는 기능들 배포
        answerList.add(count);

        // 4. List를 int[] 배열로 변환하여 반환
        return answerList.stream().mapToInt(Integer::intValue).toArray();
    }
}