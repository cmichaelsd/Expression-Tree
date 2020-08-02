from typing import Any

class Expect:
    def __init__(self, value)-> None:
        self.__value = value

    @property
    def value(self) -> Any:
        return self.__value
    
    def __message(self, condition, message):
        if condition:
            print("Passed")
        else:
            print(f"Failed: {message}")
    
    def to_equal(self, expect):
         condition = self.value == expect
         message = f"expected {expect}, result {self.value}."
         self.__message(condition, message)
            

    def to_eql(self, expect):
        condition = str(self.value) == str(expect)
        message = f"{self.value} should equal {expect}"
        self.__message(condition, message)

    def to_be(self, expect):
        condition = self.value == expect
        message = f"{self.value} should be {expect}"
        self.__message(condition, message)
