# a BinarySearchTree contains a function and a BST

class BinarySearchTree:
    def __init__(self, comes_before, node=None):
        self.node = node
        self.comes_before = comes_before
    def __eq__(self, other):
        return (type(other) == BinarySearchTree and
                self.node == other.node and
                self.comes_before == other.comes_before)
    def __repr__(self):
        rep = 'BinarySearchTree({!s}, {!r})'
        return rep.format(self.comes_before, self.node)

# a BST is one of:
# - None
# - Node
class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
    def __eq__(self, other):
        return(type(other) == Node and
               self.value == other.value and
               self.left == other.left and
               self.right == other.right)
    def __repr__(self):
        rep = 'Node({!r}, {!r}, {!r})'
        return rep.format(self.value, self.left, self.right)


# BinarySearchTree -> boolean
# returns whether or not the given BinarySearchTree is empty
def is_empty(bst):
    return bst.node is None


# BinarySearchTree value -> BinarySearchTree
# puts the value in the correct spot in the BinarySearch Tree
def insert(bst, val):
    return BinarySearchTree(bst.comes_before, bst_insert(bst.node, val, bst.comes_before))


# BST value function -> BST
# takes a BST and puts the given value in the correct spot in the tree
def bst_insert(bst, val, comes_before):
    if bst is None:
        return Node(val, None, None)
    if comes_before(val, bst.value):
        return Node(bst.value, bst_insert(bst.left, val, comes_before), bst.right)
    return Node(bst.value, bst.left, bst_insert(bst.right, val, comes_before))


# BinarySearchTree value -> boolean
# returns whether or not the given value appears in the BinarySearchTree
def lookup(bst, val):
    return lookup_help(bst.node, val, bst.comes_before)


# BST value function -> boolean
# returns whether or not the given value appears in the BST
def lookup_help(bst, val, comes_before):
    if bst is None:
        return False
    if comes_before(val, bst.value):
        return lookup_help(bst.left, val, comes_before)
    if comes_before(bst.value, val):
        return lookup_help(bst.right, val, comes_before)
    return True


# BinarySearchTree value -> BinarySearchTree
# deletes the given value (if in the tree) from a BinarySearchTree
def delete(bst, value):
    return BinarySearchTree(bst.comes_before, delete_help(bst.node, value, bst.comes_before))


# BST value -> BST
# deletes the given value from the BST (if it exists)
def delete_help(bst, val, comes_before):
    if bst is None:
        return None
    if comes_before(val, bst.value):
        return Node(bst.value,
                    delete_help(bst.left, val, comes_before),
                    bst.right)
    if comes_before(bst.value, val):
        return Node(bst.value,
                    bst.left,
                    delete_help(bst.right, val, comes_before))
    if bst.left is None:
        if bst.right is None:
            return None
        return bst.right
    if bst.right is None:
        return bst.left
    replace = find_smallest(bst.right)
    return Node(replace, bst.left, delete_help(bst.right, replace, comes_before))


# BST -> value
# finds the smallest element of a BST
def find_smallest(bst):
    if bst.left is None:
        return bst.value
    return find_smallest(bst.left)


