class MyStack:

    def __init__(self):
        self.q1= collections.deque()

    def push(self, x: int) -> None:
        q=self.q1
        q.append(x)
        for i in range(len(q)-1):
            q.append(q.popleft())

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]
        
    def empty(self) -> bool:
        return not self.q1

