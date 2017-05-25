from ctypes import py_object


class Top:

    def __init__(self):
        CTop = py_object * 10
        self.__elements = CTop()
        self.min = 0
        self.count = 0

    def add(self, new, param):
        if self.count == 10:
            value = eval("new.%s" % param)
            if value < min:
                return None
            else:
                self.__insert(new, value)
        else:
            self.__insert(new, value)

    def __insert(self, new, value):
        for index in xrange(9, -1, -1):
            if self[index].x < value:
                self.shift(index)
                new.x = value
                self[index] = new
                break
        if index == 9:
            self.min = new.x

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
            self.__pop_last
            for i in xrange(8, index, -1):
                self[i + 1] = self[i]

    def __iter__(self):
        return self

