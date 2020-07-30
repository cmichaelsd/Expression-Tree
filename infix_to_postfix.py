from stack import Stack
from typing import Any

class InfixToPostfix(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.postfix = ""
        self.__output = Stack()
        self.__priority = {
            "+": 1, 
            "-": 1, 
            "*": 2, 
            "/": 2, 
            "^": 3
        }
    
    @property
    def priority(self) -> Any:
        return self.__priority

    # Will have to change for numerals
    def is_operand(self, c) -> bool:
        return c.isalpha()

    def not_greater(self, c) -> bool:
        try:
            return self.priority[c] <= self.priority[self.peek()]
        except KeyError:
            return False

    def conversion(self, exp) -> str: 
          
        # iterate
        for c in exp:

            # if current is operand
            if self.is_operand(c): 
                # push to output
                self.__output.push(c)
              
            # if opening parentheses
            elif c  == "(": 
                # push to stack
                self.push(c) 
  
            # if closing parentheses
            elif c == ")": 
                # if stack not empty and top of stack is not opening parentheses
                while not self.is_empty() and self.peek() != "(":
                    # pop off the top of stack and push to output
                    self.__output.push(self.pop())
                # remove left over opening parentheses
                self.pop()
  
            
            else:
                # while stack is not empty and current is not greater than top of stack
                while not self.is_empty() and self.not_greater(c): 
                    # pop off top of stack until current is greater than top of stack
                    self.__output.push(self.pop())
                # push current to top of stack
                self.push(c) 
  
        # while the stack is not empty
        while not self.is_empty(): 
            # pop off top of stack and push to output
            self.__output.push(self.pop()) 
  
        self.postfix = "".join(self.__output)
