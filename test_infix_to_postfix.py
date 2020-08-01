from infix_to_postfix import InfixToPostfix
from test import Expect

expression = "1+2*(3^4-5)^(6+7*8)-9"

Expect(InfixToPostfix().conversion(expression)).to_equal("1234^5-678*+^*+9-")