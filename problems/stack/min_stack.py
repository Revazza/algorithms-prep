class MinStack:

    # list - [1, 2, 0] - add
    # max stack - [2, 2, 0] -
    # min stack - [0, 0, 0]


    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
        else:
            if self.getMin() > val:
                self.min_stack.append(val)
            else:
                self.min_stack.append(self.getMin())

        pass
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

