from typing import Any

class Stack:
    def __init__(self, *args) -> None:
        self.__top = -1
        self.array = [*args]

    @property
    def top(self) -> int:
        return self.__top

    @top.setter
    def top(self, value) -> None:
        self.__top = value
    
    @top.deleter
    def top(self, value) -> None:
        self.__top = value

    def size(self) -> int:
        return self.top
    
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

    def push(self, *argv) -> None:
        self.top += len(argv)
        self.array.extend(argv)
