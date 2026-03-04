package Programmers.Lv1.택배_상자_꺼내기;

class Solution {
    public int solution(int n, int w, int num) {
        // 1. 층수(h) 구하기 - 정수 나눗셈 올림 테크닉으로 한 줄로 축약
        int h = (n - 1) / w + 1;

        int[][] array = new int[h][w];
        int number = 1;

        // 2. 배열 채우기
        for (int i = 0; i < h; i++) {
            if (i % 2 == 0) {
                for (int j = 0; j < w && number <= n; j++) {
                    array[i][j] = number++;
                }
            } else {
                for (int j = w - 1; j >= 0 && number <= n; j--) {
                    array[i][j] = number++;
                }
            }
        }

        // 3. 꺼내야 하는 상자 계산
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                if (array[i][j] == num) {

                    int answer = 0; // 찾았을 때만 쓰이니까 여기서 선언
                    for (int r = i; r < h; r++) {
                        if (array[r][j] != 0) answer++;
                    }
                    return answer;

                }
            }
        }

        return 0; // num을 찾지 못하는 경우는 없지만, 문법상 기본 리턴값 필요
    }
}