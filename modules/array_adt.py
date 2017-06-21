from ctypes import py_object

class Array:

    def __init__(self, size):
        arr = py_object * size
        self._elements = arr()
        self._clear(0)

    def __eq__(self, other):
        for i, j in zip(self, other):
            if i != j:
                return False
        else:
            return True

    def _clear(self, value):
        for i in xrange(10):
            self._elements[i] = value

    def __getitem__(self, index):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            return self._elements[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            self._elements[index] = value
