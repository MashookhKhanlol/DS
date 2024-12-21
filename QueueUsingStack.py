
class MyQueue:

    def __init__(self):
        self.in_stack = []  # Stack for push operations
        self.out_stack = []  # Stack for pop/peek operations

    def push(self, x: int) -> None:
        self.in_stack.append(x)

    def pop(self) -> int:
        self._transfer()  # Ensure `out_stack` has elements
        return self.out_stack.pop()

    def peek(self) -> int:
        self._transfer()  # Ensure `out_stack` has elements
        return self.out_stack[-1]

    def empty(self) -> bool:
        return not self.in_stack and not self.out_stack

    def _transfer(self) -> None:
        # Transfer elements from in_stack to out_stack if out_stack is empty
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())