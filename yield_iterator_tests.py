import unittest
from linked_list import Pair, yield_iterator
class TestCases(unittest.TestCase):
    def test_yield_iterator(self):
        list = None
        for i in range(5):
            list = Pair(i, list)
        iter = yield_iterator(list)
        self.assertEqual(next(iter), 4)
        self.assertEqual(next(iter), 3)
        self.assertEqual(next(iter), 2)
        self.assertEqual(next(iter), 1)
        self.assertEqual(next(iter), 0)
        self.assertRaises(StopIteration, next, iter)

if __name__ == '__main__':
    unittest.main()