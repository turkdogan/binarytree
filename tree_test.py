#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tree import *
import unittest

def from_list(l):
    t = Tree()
    for i in l:
        t.insert(i)
    return t

def to_list(tr):
    retval = []
    tr.traverse_inorder(lambda data: retval.append(data))
    return retval

class TestTree(unittest.TestCase):

    def test_delete_root_node(self):
        sut = from_list([3, 1, 4])
        sut.remove(3)
        self.assertEqual([1, 4], to_list(sut))

    def test_delete_leaf_node(self):
        sut = from_list([3, 1, 4])
        sut.remove(4)
        self.assertEqual([1, 3], to_list(sut))

    def test_delete_node_with_two_children(self):
        sut = from_list([5, 2, 7, 1, 3, 6, 4])
        sut.remove(2)
        self.assertEqual([1, 3, 4, 5, 6, 7], to_list(sut))

    def test_delete_nodes_in_random_order(self):
        import random
        ls = [5, 2, 7, 1, 3, 6, 4]
        ord_list = sorted(ls)
        sut = from_list(ls)
        random.shuffle(ls)
        for i in ls:
            sut.remove(i)
            ord_list.remove(i)
            self.assertEqual(ord_list, to_list(sut))

    def test_reuse_tree_object(self):
        import random
        ls = [5, 2, 7, 1, 3, 6, 4]
        ord_list = sorted(ls)
        sut = from_list(ls)
        random.shuffle(ls)
        for i in ls:
            sut.remove(i)
            ord_list.remove(i)
            self.assertEqual(ord_list, to_list(sut))
        self.assertEqual([], to_list(sut))
        for i in ls:
            sut.insert(i)
        self.assertEqual(sorted(ls), to_list(sut))

    def test_find(self):
        sut = Tree()
        sut.insert('ankara', 312)
        self.assertEqual(312, sut.find('ankara'))
        sut.insert('izmir', 232)
        self.assertEqual(232, sut.find('izmir'))
        sut.insert(4815162342, 'The Island')
        self.assertEqual('The Island', sut.find(4815162342))

    def test_find_raise_exception(self):
        sut = Tree()
        with self.assertRaises(KeyError):
            sut.find('nonexistent')

if __name__ == '__main__':
    unittest.main()
