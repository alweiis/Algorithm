package Programmers.Lv1.완주하지_못한_선수;

import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        Map<String, Integer> nameMap = new HashMap<>();

        for (String name : participant) {
            nameMap.put(name, nameMap.getOrDefault(name, 0) + 1);
        }
        for (String name : completion) {
            nameMap.put(name, nameMap.get(name) - 1);
        }

        for (String name : nameMap.keySet()) {
            if (nameMap.get(name) != 0) {
                return name;
            }
        }
        return "";
    }
}
