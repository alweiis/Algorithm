class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        idx = len(self.data) - 1
        while idx > 1:
            p_idx = idx // 2
            if self.data[idx] > self.data[p_idx]:
                self.data[idx], self.data[p_idx] = self.data[p_idx], self.data[idx]
                idx = idx // 2
            else:
                break

    def remove(self):
        if len(self.data) > 1:
            self.data[1], self.data[-1] = self.data[-1], self.data[1]
            data = self.data.pop(-1)
            self.maxHeapify(1)
        else:
            data = None
        return data

    def maxHeapify(self, i):
        left = 2 * i
        right = 2 * i + 1
        smallest = i
        if left < len(self.data) and self.data[left] > self.data[smallest]:
            smallest = left
        if right < len(self.data) and self.data[right] > self.data[smallest]:
            smallest = right
        if smallest != i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.maxHeapify(smallest)


def solution(x):
    return 0
