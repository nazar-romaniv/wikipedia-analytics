import unittest
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'modules')))
import top
from random import randint


def is_reversed(ls):
    if ls.sort() == ls.reverse():
        return True
    else:
        return False


class TopTest(unittest.TestCase):
    """
    Unit test for Top. NOTE: Works with parentheses after call to getattr only!!!
    """
    def setUp(self):
        self.top = top.Top("val")
        self.default = {}

    def test_clear(self):
        self.top._clear({'val': 10})
        expected = [10] * 10
        actual = [i['val'] for i in self.top]
        self.assertItemsEqual(expected, actual)

    def test_sorted(self):
        for i in xrange(20):
            self.top.add({'val': randint(1, 200)})
        contents = [i['val'] for i in self.top]
        self.assertTrue(is_reversed(contents))

    def test_index(self):
        with self.assertRaises(IndexError):
            print self.top[10]

    def test_add(self):
        for i in xrange(9, -1, -1):
            self.top._elements[9 - i] = {'val': i}
        expected = [15] + [i for i in xrange(9, 0, -1)]
        self.top.add({'val': 15})
        actual = [i['val'] for i in self.top]
        self.assertEqual(expected, actual)

    def tearDown(self):
        del self.top


if __name__ == '__main__':
    unittest.main(verbosity=2)
