from typing import Any

class Stack:
    def __init__(self):
        self.top = -1
        self.array = []
    
    def is_empty(self) -> bool:
        if self.top == -1:
            return True
        return False
    
    def peek(self) -> Any:
        return self.array[-1]

    def pop(self) -> Any:
        if not self.is_empty():
            self.top -= 1
            return self.array.pop()
        return "$"

    def push(self, value):
        self.top += 1
        self.array.append(value)
