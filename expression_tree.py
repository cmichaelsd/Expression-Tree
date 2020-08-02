from infix_to_postfix import InfixToPostfix
from stack import Stack
from typing import Any
from ctypes import Array

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree():
    def __init__(self, expression) -> None:
        self.postfix = str(InfixToPostfix(expression))
        self.__tree = Stack()
        self.__construct()

    @property
    def tree(self) -> Any:
        return self.__tree

    def __is_operand(self, c) -> bool:
        return c.isdigit()

    def __construct(self) -> None:
        # iterate postfix
        for c in self.postfix:
            # if c is operand
            if self.__is_operand(c):
                # create node
                t = Node(c)
                # push node
                self.tree.push(t)
            else:
                # if c is an operator
                # create node
                t = Node(c)

                ###
                # will always have two elements to pop
                # ex: 12+

                # pop last node from the list
                # set node as right
                t.right = self.tree.pop()
                # pop last node from the list
                # set node as left
                t.left = self.tree.pop()
                # push node
                self.tree.push(t)

    def in_order_traversal(self) -> Array:
        # get the root of the tree
        cur = self.tree.peek()
        # init a stack
        s = Stack()
        output = Stack()

        while cur is not None or not s.is_empty():
            # if node exists
            if cur is not None:
                # move to the left most node
                # push current
                s.push(cur)
                # set current to nodes left
                cur = cur.left
            elif not s.is_empty():
                # if stack is not empty
                # set current to last element in stack
                cur = s.pop()
                # print currents value
                output.push(cur.value)
                # set current to nodes right
                cur = cur.right

        return output.array
    
    def evaluate(self) -> int:

        def recurse(n) -> int:
            # if both node children are none
            if n.right is None and n.left is None:
                # return nodes value cast as an integer
                return int(n.value)

            ###
            # gather left most nodes value of this function
            # if left is none and right exists
            # right recurses and right left becomes l
            l = recurse(n.left)
            r = recurse(n.right)

            # evaluate base on nodes operator
            if n.value == '+': return l + r
            if n.value == '-': return l - r
            if n.value == '*': return l * r
            if n.value == '/': return l / r
            if n.value == '^': return l ** r
        return recurse(self.tree.peek())
