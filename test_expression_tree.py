from expression_tree import ExpressionTree
from test import Expect

expressionTree = ExpressionTree("1+2*(3^4-5)^(6+7*8)-9")
Expect(expressionTree.in_order_traversal()).to_eql(['1', '+', '2', '*', '3', '^', '4', '-', '5', '^', '6', '+', '7', '*', '8', '-', '9'])
Expect(expressionTree.evaluate()).to_be(815591549033893628845280316807892455704843888770177860370834864518732819193118385174402429555778063881417457299095544)