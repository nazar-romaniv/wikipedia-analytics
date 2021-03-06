from array_adt import ArrayADT


class Top(ArrayADT):

    def __init__(self, param):
        CTop = py_object * 10
        self.param = param
        self._elements = CTop()
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

    def add(self, val, page_id):
        if val < self.min:
            return None
        else:
            for index in xrange(0, 10):
                if self[index][1] < val:
                    self._shift(index)
                    self[index] = (page_id, val)
                    break
            if index == 9:
                self.min = val

    def display(self):
        print 'Top 10 pages by %s:' % self.param
        for page in self:
            print 'ID: %d, %s: %d' % (page[0], self.param, page[1])

    def __getitem__(self, index):
        if index < 0 or index >= 10:
            raise IndexError("Array has %d elements" % len(self))
        else:
            return self._elements[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= 10:
            raise IndexError("Array has %d elements" % len(self))
        else:
            self._elements[index] = value

    def _shift(self, index):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            for i in xrange(8, index - 1, -1):
                self[i + 1] = self[i]

    def __iter__(self):
        return _ArrayIterator(self)


class _ArrayIterator:

    def __init__(self, arr):
        self.current = 0
        self.arr = arr

    def __iter__(self):
        return self

    def next(self):
        if self.current == 10:
            raise StopIteration
        else:
            obj = self.arr[self.current]
            self.current += 1
            return obj
