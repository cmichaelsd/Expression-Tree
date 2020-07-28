from infix_to_postfix import InfixToPostfix

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class ExpressionTree(InfixToPostfix):
    def __init__(self, expression):
        InfixToPostfix.__init__(self)
        self.tree = []
        self.conversion(expression)
        self.construct()
        self.in_order_traversal(self.tree.pop())

    def in_order_traversal(self, n) -> None:
        if n is not None:
            self.in_order_traversal(n.left)
            print(n.value)
            self.in_order_traversal(n.right)

    def is_operator(self, c) -> bool:
        if c in self.priority:
            return True
        return False

    def construct(self) -> None:
        for c in self.postfix:
            if not self.is_operator(c):
                t = Node(c)
                self.tree.append(t)
            else:
                t = Node(c)
                t.right = self.tree.pop()
                t.left = self.tree.pop()

                self.tree.append(t)

expressionTree = ExpressionTree("a+b*(c^d-e)^(f+g*h)-i")
print(expressionTree.postfix)
