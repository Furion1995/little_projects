"""
    Modify the ArrayStack implementation so that the stack’s capacity is limited
    to 'maxlen' elements, where 'maxlen' is an optional parameter to the
    constructor (that defaults to None). If push method is called when the stack is at
    full capacity, throw a 'Full' exception (defined similarly to Empty).
"""


class Empty(Exception):
    pass


class Full(Exception):
    pass


class ArrayStack:

    def __init__(self, maxlen=None):
        self._data = []
        self._maxlen = maxlen

    def __len__(self):
        return len(self._data)

    def is_empty(self) -> object:
        return len(self._data) == 0

    def push(self, e):
        if len(self._data) == self._maxlen:
            raise Full('Stack at full capacity')
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

    def __str__(self) -> str:
        return str(self._data)
