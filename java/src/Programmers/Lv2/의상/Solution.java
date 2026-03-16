package Programmers.Lv2.의상;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        Map<String, Integer> map = new HashMap<>();
        for (String[] item : clothes) {
            map.put(item[1], map.getOrDefault(item[1], 0) + 1);
        }
        for (int count: map.values()) {
            answer *= (count + 1);
        }
        return answer - 1;
    }
}
