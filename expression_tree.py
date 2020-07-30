from infix_to_postfix import InfixToPostfix
from stack import Stack
from typing import Any

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree(InfixToPostfix):
    def __init__(self, expression) -> None:
        InfixToPostfix.__init__(self)
        self.__tree = Stack()
        self.conversion(expression)
        self.__construct()
        self.in_order_traversal(self.tree.pop())

    @property
    def tree(self) -> Any:
        return self.__tree

    def in_order_traversal(self, n) -> None:
        if n is not None:
            self.in_order_traversal(n.left)
            print(n.value)
            self.in_order_traversal(n.right)

    def __is_operator(self, c) -> bool:
        if c in self.priority:
            return True
        return False

    def __construct(self) -> None:
        for c in self.postfix:
            if not self.__is_operator(c):
                t = Node(c)
                self.tree.push(t)
            else:
                t = Node(c)
                t.right = self.tree.pop()
                t.left = self.tree.pop()

                self.tree.push(t)

expressionTree = ExpressionTree("a+b*(c^d-e)^(f+g*h)-i")
print(expressionTree.postfix)
