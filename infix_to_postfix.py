from stack import Stack
from typing import Any

class InfixToPostfix(Stack):
    def __new__(cls, expression) -> str:
        instance = super(InfixToPostfix, cls).__new__(cls)
        instance.__init__(expression)
        return instance.__conversion()

    def __init__(self, expression) -> None:
        Stack.__init__(self)
        self.expression = expression
        self.__output = Stack()
        self.__priority = {
            "+": 1, 
            "-": 1, 
            "*": 2, 
            "/": 2, 
            "^": 3
        }

    @property
    def output(self) -> Any:
        return self.__output
    
    @property
    def priority(self) -> Any:
        return self.__priority

    def __is_operand(self, c) -> bool:
        return c.isdigit()

    def __not_greater(self, c) -> bool:
        try:
            return self.priority[c] <= self.priority[self.peek()]
        except KeyError:
            return False

    def __conversion(self) -> str: 
        
        # iterate
        for c in self.expression:

            # if current is operand
            if self.__is_operand(c): 
                # push to output
                self.output.push(c)
              
            # if opening parentheses
            elif c  == "(": 
                # push to stack
                self.push(c) 
  
            # if closing parentheses
            elif c == ")": 
                # if stack not empty and top of stack is not opening parentheses
                while not self.is_empty() and self.peek() != "(":
                    # pop off the top of stack and push to output
                    self.output.push(self.pop())
                # remove left over opening parentheses
                self.pop()
  
            
            else:
                # while stack is not empty and current is not greater than top of stack
                while not self.is_empty() and self.__not_greater(c): 
                    # pop off top of stack until current is greater than top of stack
                    self.output.push(self.pop())
                # push current to top of stack
                self.push(c) 
  
        # while the stack is not empty
        while not self.is_empty(): 
            # pop off top of stack and push to output
            self.output.push(self.pop()) 
  
        return "".join(self.output.array)
