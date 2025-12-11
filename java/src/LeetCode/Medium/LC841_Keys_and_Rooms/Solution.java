package LeetCode.Medium.LC841_Keys_and_Rooms;

import java.util.List;

class Solution {
    private boolean[] visited;
    private int visitedCount = 0;

    public boolean canVisitAllRooms(List<List<Integer>> rooms) {
        int n = rooms.size();
        visited = new boolean[n];
        visitedCount = 0;

        visited[0] = true;
        visitedCount++;

        dfs(0, rooms);

        return visitedCount == n;
    }

    private void dfs(int room, List<List<Integer>> rooms) {
        for (int key : rooms.get(room)) {
            if (!visited[key]) {
                visited[key] = true;
                visitedCount++;
                dfs(key, rooms);
            }
        }
    }
}