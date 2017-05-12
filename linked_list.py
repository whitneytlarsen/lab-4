import sys
sys.setrecursionlimit(1000100)

# an AnyList is one of:
# - None
# - Pair(Any, AnyList)
# a first is a value of any type and makes up the first part of Pair
# a rest is an AnyList and makes up the rest of Pair

class Pair:
    def __init__(self, first, rest):
        self.first = first # any type
        self.rest = rest #AnyList
    def __repr__(self):
        return 'Pair({!r}, {!r})'.format(self.first, self.rest)
    def __eq__(self, other):
        return type(other) == Pair and other.first == self.first and other.rest == self.rest



# -> AnyList
# takes no arguments and returns an empty list
def empty_list():
    return None

# a list is an AnyList on which the function should act
# an index is an integer representing the location at which the function is supposed to do something
# a val is a value of any type representing the value that should be put into the list
# a current is an integer representing the current location of the function in the list
# AnyList integer Any -> AnyList
# returns an AnyList with the same elements as the first list, but with the given value at the given index
def add(list, index, val, current=0):
    if (type(list) != Pair and index > current) or index < 0:
        raise IndexError()
    if current == index:
        return Pair(val, list)
    return Pair(list.first, add(list.rest, index, val, current + 1))

# a len is an integer representing the length of the list up to the current position
# AnyList -> integer
# takes a list and returns an integer representing the length of the list
def length(list, len=0):
    if type(list) != Pair:
        return len
    return length(list.rest, len + 1)

# an index is an integer representing a position in a list
# a current is an integer representing the current index in the list
# AnyList integer -> AnyList
# takes a list and an index and returns the value at the index position of the list
def get(list, index, current=0):
    if type(list) != Pair or index < 0:
        raise IndexError()
    if current == index:
        return list.first
    return get(list.rest, index, current + 1)

# AnyList integer Any -> AnyList
# changes the value at the given index of the list to the given value
def set(list, index, value, current=0):
    if type(list) != Pair or index < 0:
        raise IndexError()
    if index == current:
        return Pair(value, list.rest)
    return Pair(list.first, set(list.rest, index, value, current + 1))

# AnyList integer -> AnyList
# takes a list and an index and returns the list with the value at the given index removed
def remove(list, index, current=0):
    if type(list) != Pair or index < 0:
        raise IndexError()
    if current == index:
        return (list.first,list.rest)
    return remove(list.rest, index, current + 1)[0], Pair(list.first, remove(list.rest, index, current + 1)[1])

# value value -> boolean
# used for testing sort
def gen_less_than(value1, value2):
    if value1 != value2:
        return value1 <value2

# AnyList method -> AnyList
# takes a list and a comparator method of the attributes of that list and returns the list sorted based on the comparator
def sort(list, comparator, sorted=empty_list()):
    if list is None:
        return sorted
    sorted = sort_help(list.first, comparator, sorted)
    return sort(list.rest, comparator, sorted)


# value method AnyList -> AnyList
# takes a value, a method, and a list and places the value
# in the correct place in the list based on the method
def sort_help(value, comparator, sorted):
    if sorted is None:
        return Pair(value, None)
    if comparator(value, sorted.first):
        return Pair(value, sorted)
    return Pair(sorted.first, sort_help(value, comparator, sorted.rest))

# AnyList function -> AnyList
# Applies the givene function to every element of the list
def foreach(list, func):
    if list is None:
        return None
    return Pair(func(list.first), foreach(list.rest, func))


# an Iterator represents a pointer keeping track of the position in a list
class Iterator:
    def __init__(self, list):
        self.list = list
    def __repr__(self):
        return 'Iterator({!r})'.format(self.list)
    def __eq__(self, other):
        return type(other) == Iterator and other.list == self.list


# LinkedList -> Iterator
# takes a linked list and returns an Iterator for the list
def object_iterator(list):
    return Iterator(list)


# Iterator -> boolean
# returns whether or not there is another object in the iterated list
def has_next(iter):
    return not(iter.list is None or iter.list.rest is None)


# Iterator -> value
# returns the next value in the Iterator's list and moves the iterator forward in the list
def next(iter):
    if iter.list is None or iter.list.rest is None:
        raise StopIteration()
    iter.list = iter.list.rest
    return iter.list.first

# LinkedList -> value
# takes a linked list and yields every value of the list
def yield_iterator(list):
    if list is not None:
        yield list.first
        yield from(yield_iterator(list.rest))


