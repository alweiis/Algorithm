package LeetCode.Medium.LC2352_Equal_Row_and_Column_Pairs;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int equalPairs(int[][] grid) {
        int n = grid.length;
        Map<String, Integer> rowCount = new HashMap<>();
        StringBuilder sb;

        // 1) 각 행을 안전한 문자열 키로 만들어 Map에 카운트 저장
        // 구분자로 '#' 사용 (숫자와 겹치지 않는 문자)
        for (int r = 0; r < n; r++) {
            sb = new StringBuilder();
            for (int c = 0; c < n; c++) {
                sb.append(grid[r][c]).append('#'); // 숫자 뒤에 구분자 추가
            }
            String key = sb.toString();
            rowCount.merge(key, 1, Integer::sum);
        }

        // 2) 각 열을 같은 방식으로 문자열 키 생성 후, Map에서 빈도 가져와 정답 누적
        int answer = 0;
        for (int c = 0; c < n; c++) {
            sb = new StringBuilder();
            for (int r = 0; r < n; r++) {
                sb.append(grid[r][c]).append('#');
            }
            String key = sb.toString();
            answer += rowCount.getOrDefault(key, 0);
        }
        return answer;
    }
}