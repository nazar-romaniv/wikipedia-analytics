from ctypes import py_object

class ArrayADT:

    def __init__(self, size):
        arr = py_object * 10
        self._elements = arr()
        self.min = 0
        self._clear((0, 0))


    def __eq__(self, other):
        for i, j in zip(self, other):
            if i != j:
                return False
        else:
            return True


    def _clear(self, value):
        for i in xrange(10):
            self._elements[i] = value