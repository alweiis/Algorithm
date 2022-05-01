class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [row.count(1) for row in mat]
        chk, ans = [], []
        for idx, val in enumerate(soldiers):
            chk.append((val, idx))
        chk.sort(key=lambda x: x[0])
        for i in range(k):
            ans.append(chk[i][1])
        return ans