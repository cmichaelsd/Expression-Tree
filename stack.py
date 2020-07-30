from typing import Any

class Stack:
    def __init__(self):
        self.__top = -1
        self.__array = []

    @property
    def top(self) -> int:
        return self.__top

    @top.setter
    def top(self, value):
        self.__top = value
    
    @top.deleter
    def top(self, value):
        self.__top = value
    
    def is_empty(self) -> bool:
        if self.top == -1:
            return True
        return False
    
    def peek(self) -> Any:
        return self.__array[-1]

    def pop(self) -> Any:
        if not self.is_empty():
            self.top -= 1
            return self.__array.pop()
        return "$"

    def push(self, value) -> None:
        self.top += 1
        self.__array.append(value)
