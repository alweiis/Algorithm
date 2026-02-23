package Programmers.Lv2.주차_요금_계산;

import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int baseTime = fees[0];
        int baseFee = fees[1];
        int unitTime = fees[2];
        int unitFee = fees[3];

        Map<String, Integer> inMap = new HashMap<>();
        Map<String, Integer> totalMap = new TreeMap<>();

        for (String record : records) {
            String[] parts = record.split(" ");
            int time = toMinutes(parts[0]);
            String car = parts[1];
            String type = parts[2];

            if (type.equals("IN")) {
                inMap.put(car, time);
            } else {
                int inTime = inMap.remove(car);
                int parkingTime = time - inTime;

                totalMap.put(car,
                        totalMap.getOrDefault(car, 0) + parkingTime);
            }
        }

        // 23:59 처리
        int endTime = toMinutes("23:59");

        for (String car : inMap.keySet()) {
            int inTime = inMap.get(car);
            int parkingTime = endTime - inTime;

            totalMap.put(car,
                    totalMap.getOrDefault(car, 0) + parkingTime);
        }

        // 요금 계산
        int[] answer = new int[totalMap.size()];
        int idx = 0;

        for (int totalTime : totalMap.values()) {
            if (totalTime <= baseTime) {
                answer[idx++] = baseFee;
            } else {
                int extraTime = totalTime - baseTime;
                int units = (extraTime + unitTime - 1) / unitTime; // 올림 처리
                answer[idx++] = baseFee + units * unitFee;
            }
        }
        return answer;
    }

    private int toMinutes(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }
}