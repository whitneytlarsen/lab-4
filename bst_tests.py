import unittest
from bst import *


# number number -> boolean
# used for testing sort
def gen_less_than(value1, value2):
    if value1 != value2:
        return value1 < value2

# string string -> boolean


class TestCases(unittest.TestCase):
    def test_node_repr(self):
        self.assertEqual(str(Node(1, None, None)), 'Node(1, None, None)')
    def test_bst_repr(self):
        bst = BinarySearchTree(gen_less_than, Node(1, None, None))
        self.assertEqual(str(bst),
                         'BinarySearchTree({!r}, Node(1, None, None))'.format(bst.comes_before))
    def test_is_empty(self):
        self.assertTrue(is_empty(BinarySearchTree(gen_less_than, None)))
        self.assertFalse(is_empty(BinarySearchTree(gen_less_than, Node(12, None, None))))
    def test_insert(self):
        self.assertEqual(insert(BinarySearchTree(gen_less_than, None), 1),
                                BinarySearchTree(gen_less_than, Node(1, None, None)))
        bst = BinarySearchTree(gen_less_than, Node(2, Node(1, None, None), Node(4, None, None)))
        self.assertEqual(insert(bst, 0),
                         BinarySearchTree(gen_less_than,
                                          Node(2, Node(1, Node(0, None, None), None),
                                               Node(4, None, None))))
        self.assertEqual(insert(bst, 3),
                         BinarySearchTree(gen_less_than,
                                          Node(2, Node(1, None, None),
                                               Node(4, Node(3, None, None), None))))
    def test_bst_insert(self):
        bst = Node(3, Node(1, None, None), Node(5, None, None))
        self.assertEqual(bst_insert(bst, 2, gen_less_than),
                         Node(3, Node(1, None, Node(2, None, None)),
                              Node(5, None, None)))
        self.assertEqual(bst_insert(bst, 4, gen_less_than),
                         Node(3, Node(1, None, None),
                              Node(5, Node(4, None, None), None)))
    def test_lookup(self):
        bst = BinarySearchTree(gen_less_than,
                               Node(3, Node(1, None, None),
                                    Node(5, None, None)))
        self.assertFalse(lookup(BinarySearchTree(gen_less_than), 1))
        self.assertTrue(lookup(bst, 1))
        self.assertTrue(lookup(bst, 5))
        self.assertFalse(lookup(bst, 2))
        self.assertFalse(lookup(bst, 4))
    def test_lookup_help(self):
        bst = Node(3, Node(1, None, None), Node(5, None, None))
        self.assertFalse(lookup_help(None, 1, gen_less_than))
        self.assertTrue(lookup_help(bst, 3, gen_less_than))
        self.assertTrue(lookup_help(bst, 1, gen_less_than))
        self.assertTrue(lookup_help(bst, 5, gen_less_than))
    def test_delete(self):
        bst = BinarySearchTree(gen_less_than,
                               Node(3, Node(1, None, None),
                                    Node(5, None, None)))
        bst1 = delete(bst, 1)
        bst2 = delete(bst, 5)
        self.assertEqual(delete(BinarySearchTree(gen_less_than, None), 1),
                         BinarySearchTree(gen_less_than, None))
        self.assertEqual(delete(bst, 3),
                         BinarySearchTree(gen_less_than,
                                          Node(5, Node(1, None, None), None)))
        self.assertEqual(delete(bst, 5),
                         BinarySearchTree(gen_less_than,
                                          Node(3,
                                               Node(1, None, None),
                                               None)))
        self.assertEqual(delete(bst1, 3),
                         BinarySearchTree(gen_less_than,
                                          Node(5, None, None)))
        self.assertEqual(delete(bst2, 3),
                         BinarySearchTree(gen_less_than,
                                          Node(1, None, None)))
    def test_delete_help(self):
        bst = Node(3, Node(1, None, None), Node(5, None, None))
        bst1 = delete_help(bst, 1, gen_less_than)
        bst2 = delete_help(bst, 5, gen_less_than)
        self.assertEqual(delete_help(None, 1, gen_less_than), None)
        self.assertEqual(delete_help(bst, 3, gen_less_than),
                         Node(5, Node(1, None, None), None))
        self.assertEqual(delete_help(bst, 5, gen_less_than),
                         Node(3, Node(1, None, None), None))
        self.assertEqual(delete_help(bst1, 3, gen_less_than),
                         Node(5, None, None))
        self.assertEqual(delete_help(bst2, 3, gen_less_than),
                         Node(1, None, None))
    def test_find_smallest(self):
        bst = Node(3, Node(1, None, None), Node(5, None, None))
        self.assertEqual(find_smallest(bst), 1)

if __name__ == '__main__':
    unittest.main()