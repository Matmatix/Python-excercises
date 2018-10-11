import unittest
from LinkedList import LinkedList


class LLTestCase(unittest.TestCase):

    def test_create(self):
        ''' Test creation of Linked List'''
        ll = LinkedList()

    def test_add(self):
        ''' Test adding node to LL '''
        LL.add_node(1)
        LL.add_node(2)
        LL.add_node(4)
        LL.add_node(3)

    def test_remove(self):
        ''' Test removing node from LL '''
        LL.remove_node(3)

    def test_print(self):
        ''' Test removing node from LL '''
        LL.print_ll()

    def test_reverse(self):
        ''' Test removing node from LL '''
        reversed_LL = LL.reverse()
        for item in reversed_LL:
            print(item.data)

LL = LinkedList()

unittest.main()


