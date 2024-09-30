
# My Solution
class CustomStack:
    def __init__(self, max_size: int):
        self._stack = [0] * max_size
        self._inc = [0] * max_size
        self._top = -1
    def push(self, x: int) -> None:
        if self._top < len(self._stack) - 1:
            self._top += 1
            self._stack[self._top] = x
    def pop(self) -> int:
        if self._top < 0:
            return -1
        result = self._stack[self._top] + self._inc[self._top]
        if self._top > 0:
            self._inc[self._top - 1] += self._inc[self._top]
        self._inc[self._top] = 0
        self._top -= 1
        return result
    def increment(self, k: int, val: int) -> None:
        if self._top >= 0:
            index = min(self._top, k - 1)
            self._inc[index] += val

# Best / Most Optimal Solution
class CustomStack:
    def __init__(self, maxSize: int):
        self.stack = []
        self.maxSize = maxSize
        self.inc = []
    def push(self, x: int) -> None:
        if len(self.stack) == self.maxSize:
            return
        self.stack.append(x)
        self.inc.append(0)
    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        if len(self.inc) > 1:
            self.inc[-2] += self.inc[-1]
        return self.stack.pop() + self.inc.pop()
    def increment(self, k: int, val: int) -> None:
        k = min(k, len(self.stack))
        if k == 0:
            return
        self.inc[k - 1] += val

