package LeetCode.Medium.LC649_Dota2_Senate;

import java.util.Queue;
import java.util.ArrayDeque;

class Solution {
    public String predictPartyVictory(String senate) {
        Queue<Character> queue = new ArrayDeque<>();
        int radiantCount = 0;
        int direCount = 0;

        // 초기 큐 구성 및 각 진영 카운트
        for (char ch : senate.toCharArray()) {
            queue.offer(ch);
            if (ch == 'R') radiantCount++;
            else direCount++;
        }

        int bannedRadiant = 0; // 다음에 등장하는 R을 제거할 권한 수
        int bannedDire = 0;    // 다음에 등장하는 D을 제거할 권한 수

        // 양쪽 진영이 남아있는 동안 반복
        while (radiantCount > 0 && direCount > 0) {
            char cur = queue.poll(); // null일 가능성 없음(문제 조건)
            if (cur == 'R') {
                if (bannedRadiant > 0) {
                    // 이 R은 금지되었으므로 제거 처리
                    bannedRadiant--;
                    radiantCount--;
                    continue;
                }
                // 이 R은 살아남아 라운드 끝에 다시 대기열에 들어가며,
                // 상대 진영(D) 중 하나를 금지할 권한을 얻음
                queue.offer(cur);
                bannedDire++;
            } else { // cur == 'D'
                if (bannedDire > 0) {
                    bannedDire--;
                    direCount--;
                    continue;
                }
                queue.offer(cur);
                bannedRadiant++;
            }
        }

        return radiantCount > 0 ? "Radiant" : "Dire";
    }
}