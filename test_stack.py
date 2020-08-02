from test import Expect
from stack import Stack

s = Stack()

s.push("a", "b", "c")

Expect(s.array).to_eql(["a", "b", "c"])
Expect(s.size()).to_be(2)
Expect(s.peek()).to_equal("c")
Expect(s.pop()).to_equal("c")
Expect(s.array).to_eql(["a", "b"])
s.pop()
s.pop()
Expect(s.is_empty()).to_be(True)
