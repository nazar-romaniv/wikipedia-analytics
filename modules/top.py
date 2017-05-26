from ctypes import py_object


class Top:

    def __init__(self, param):
        CTop = py_object * 10
        self._param = param
        self._elements = CTop()
        self.min = 0
        self._clear(None)

    def _clear(self, value):
        for i in xrange(10):
            self._elements[i] = value

    def add(self, new):
        if new < min:
            return None
        else:
            self._insert(new)

    def _insert(self, new):
        for index in xrange(0, 10):
            if self[index] < new:
                self._shift(index)
                self[index] = new
                break
        if index == 9:
            self.min = new

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

    def _shift(self, index):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            for i in xrange(8, index - 1, -1):
                self[i + 1] = self[i]

    def __iter__(self):
        return _TopIterator(self)


class _TopIterator:

    def __init__(self, top):
        self.current = 0
        self.top = top

    def __iter__(self):
        return self

    def next(self):
        if self.current == 10:
            raise StopIteration
        else:
            obj = self.top[self.current]
            self.current += 1
            return obj
