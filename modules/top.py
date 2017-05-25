from ctypes import py_object


class Top:

    def __init__(self, param):
        CTop = py_object * 10
        self.__param = param
        self.__elements = CTop()
        self.min = 0
        self.count = 0
        self.__clear(None)

    def __clear(self, value):
        for i in xrange(10):
            self.__elements[i] = value

    def view(self):
        for item, index in enumerate(self):
            print item, index

    def add(self, new):
        if self.count == 10:
            if new < min:
                return None
            else:
                self.__insert(new)
        else:
            self.__insert(new)

    def __insert(self, new):
        for index in xrange(0, 10):
            if self[index] < new:
                self.__shift(index)
                self[index] = new
                break
        if index == 9:
            self.min = new

    def __getitem__(self, index):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            return self.__elements[index]

    def __setitem__(self, index, value):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            self.__elements[index] = value

    def __shift(self, index):
        if index < 0 or index >= 10:
            raise IndexError("Top only contains top 10 items")
        else:
            for i in xrange(8, index, -1):
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

