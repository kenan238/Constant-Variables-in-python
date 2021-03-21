import os, sys

class ChangeConstantError(Exception):
    pass

class const:
    def __init__(self, val):
        self.val = val
    @property
    def value(self): return self.val

    @value.setter
    def value(self, newval):
        raise ChangeConstantError("Cannot modify a constant variable's value!")
#Usage:
# a=const("e")
# print(a.value)
# a.value="a" #will give an error
