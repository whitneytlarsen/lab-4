import unittest
from linked_list import *

class TestCases(unittest.TestCase):
    def test_repr(self):
        self.assertEqual(str(Iterator(None)), 'Iterator(None)')
        self.assertEqual(str(Iterator(Pair(1, None))),
                         'Iterator(Pair(1, None))')
    def test_object_iterator(self):
        self.assertEqual(object_iterator(None), Iterator(None))
        self.assertEqual(object_iterator(Pair(1, None)),
                                         Iterator(Pair(1, None)))
    def test_has_next(self):
        self.assertFalse(has_next(Iterator(None)))
        self.assertFalse(has_next(Iterator(Pair(1, None))))
        self.assertTrue(has_next(Iterator(Pair(1, Pair(2, None)))))
    def test_next(self):
        iter = object_iterator(Pair(1, Pair(2, Pair(3, None))))
        self.assertEqual(next(iter), 2)
        self.assertEqual(iter, Iterator(Pair(2, Pair(3, None))))
        self.assertEqual(next(iter), 3)
        self.assertEqual(iter, Iterator(Pair(3, None)))
        self.assertRaises(StopIteration, next, iter)

if __name__ == '__main__':
    unittest.main()