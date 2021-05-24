from typing import Any

class Stack:
    def __init__(self) -> None:
        self._stack = []

    def push(self, val) -> None:
        self._stack.append(val)

    def pop(self) -> Any:
        return self._stack.pop(len(self._stack) - 1)

    def top(self) -> str:
        return self._stack[len(self._stack) - 1]


class Solution:
    def isValid(self, s: str) -> bool:
        openers = ["(", "[", "{"]
        closers = [")", "]", "}"]

        stack = Stack()
        for ch in s:
            if ch in openers:
                stack.push(ch)
            elif ch in closers:
                if len(stack) > 0:
                    last = stack.pop()

                    # if the last value in the stack is the corresponding bracket,
                    # we are good (each list is the same length)
                    open_i = closers.index(ch)
                    opener = openers[open_i]

                    if last != opener:
                        return False

                else:
                    # stack is non-empty AND no opener recorded
                    return False

        # handle the case where there is only one opener and no closer
        # each bracket should be accounted for
        if len(stack) != 0:
            return False

        return True
