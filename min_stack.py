class MinStack:
    def __init__(self) -> None:
        self._stack = []

    def push(self, val: int) -> None:
        self._stack.append(val)

    def pop(self) -> None:
        self._stack.pop(len(self._stack) - 1)

    def top(self) -> int:
        return self._stack[len(self._stack) - 1]

    def getMin(self) -> int:
        return sorted(self._stack)[0]

def main():
    obj = MinStack()
    obj.push(3)
    obj.push(4)
    obj.push(5)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()

    assert param_3 == 4
    assert param_4 == 3


if __name__ == "__main__":
    main()
