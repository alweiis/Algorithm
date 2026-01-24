package LeetCode.Medium.LC399_Evaluate_Division;

import java.util.*;

class Solution {
    // 인접 리스트 그래프
    private Map<String, List<Edge>> graph = new HashMap<>();

    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        // 1. 그래프 생성
        buildGraph(equations, values);

        // 2. 쿼리 처리
        double[] result = new double[queries.size()];

        for (int i = 0; i < queries.size(); i++) {
            String start = queries.get(i).get(0);
            String end = queries.get(i).get(1);

            // 기본적으로 계산 불가능한 경우
            if (!graph.containsKey(start) || !graph.containsKey(end)) {
                result[i] = -1.0;
                continue;
            }

            // 자기 자신을 나누는 경우
            if (start.equals(end)) {
                result[i] = 1.0;
                continue;
            }

            // 탐색 시작
            Set<String> visited = new HashSet<>();
            result[i] = dfs(start, end, 1.0, visited);
        }

        return result;
    }

    // 그래프 구성
    private void buildGraph(List<List<String>> equations, double[] values) {
        for (int i = 0; i < equations.size(); i++) {
            String a = equations.get(i).get(0);
            String b = equations.get(i).get(1);
            double value = values[i];

            graph.computeIfAbsent(a, _ -> new ArrayList<>()).add(new Edge(b, value));
            graph.computeIfAbsent(b, _ -> new ArrayList<>()).add(new Edge(a, 1.0 / value));
        }
    }

    // 핵심 탐색 로직 (의사코드의 search 함수)
    private double dfs(String current, String target, double accumulated, Set<String> visited) {
        // 목표 도달
        if (current.equals(target)) {
            return accumulated;
        }

        visited.add(current);
        for (Edge edge : graph.get(current)) {
            if (!visited.contains(edge.node)) {
                double result = dfs(edge.node, target, accumulated * edge.weight, visited);

                // 경로를 찾은 경우 즉시 반환
                if (result != -1.0) {
                    return result;
                }
            }
        }
        // 어떤 경로로도 도달하지 못한 경우
        return -1.0;
    }

    // 인접 리스트용 간선 클래스
    static class Edge {
        String node;
        double weight;

        Edge(String node, double weight) {
            this.node = node;
            this.weight = weight;
        }
    }
}
