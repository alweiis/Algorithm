package LeetCode.Medium.LC1466_Reorder_Routes_to_Make_All_Paths_Lead_to_the_City_Zero;

import java.util.ArrayList;
import java.util.List;

class Solution {

    // 인접 리스트: 각 노드에서 (다음 노드, 방향 비용)
    private List<int[]>[] graph;
    private boolean[] visited;
    private int answer = 0;

    public int minReorder(int n, int[][] connections) {
        graph = new ArrayList[n];
        visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            graph[i] = new ArrayList<>();
        }

        // 그래프 구성
        for (int[] conn : connections) {
            int from = conn[0];
            int to = conn[1];

            // 원래 방향: from -> to (뒤집어야 하므로 cost = 1)
            graph[from].add(new int[]{to, 1});

            // 반대 방향: to -> from (이미 올바른 방향, cost = 0)
            graph[to].add(new int[]{from, 0});
        }

        // 0번 도시에서 DFS 시작
        dfs(0);

        return answer;
    }

    private void dfs(int current) {
        visited[current] = true;

        for (int[] next : graph[current]) {
            int nextCity = next[0];
            int cost = next[1];

            if (!visited[nextCity]) {
                // 원래 방향이 바깥쪽이면 뒤집어야 함
                answer += cost;
                dfs(nextCity);
            }
        }
    }
}