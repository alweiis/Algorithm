package Programmers.Lv2.전화번호_목록;

import java.util.HashMap;
import java.util.Map;

class Solution {
    public boolean solution(String[] phone_book) {
        Map<String, Integer> map = new HashMap<>();

        for (String phone : phone_book) {
            map.put(phone, 1);
        }

        for (String phone : phone_book) {
            // 본인 전체 길이 전까지만 자르기 위해 phone.length() 미만으로 설정
            for (int i = 1; i < phone.length(); i++) {
                String prefix = phone.substring(0, i);

                if (map.containsKey(prefix)) {
                    return false;
                }
            }
        }
        return true;
    }
}