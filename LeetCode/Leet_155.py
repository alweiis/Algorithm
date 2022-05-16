class MinStack:

    def __init__(self):
        self.data = []

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        del self.data[-1]

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return min(self.data)