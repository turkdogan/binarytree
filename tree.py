#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Node(object):
    """docstring for Node"""
    def __init__(self, key, value=None):
        super(Node, self).__init__()
        self.left = [None]
        self.right = [None]
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key)


def deref(ref):
    return ref[0]

def setref(ref, val):
    ref[0] = val


class Tree(object):
    """docstring for Tree"""
    def __init__(self):
        super(Tree, self).__init__()
        self.root = [None]

    # Since Python doesn't support tail-call optimization, I think
    # it is better to insert iteratively.
    def insert(self, key, value=None):
        curr = self.root
        while True:
            if deref(curr) is None:
                setref(curr, Node(key, value))
                break
            if key < deref(curr).key:
                curr = deref(curr).left
            else:
                curr = deref(curr).right

    def remove(self, key):
        node = self._find(key)
        self._remove(node)

    def find(self, key):
        return deref(self._find(key)).value

    def traverse_inorder(self, fn):
        stack = []
        curr = deref(self.root)

        while True:
            while curr:
                stack.append(curr)
                curr = deref(curr.left)

            if stack:
                curr = stack.pop()
                fn(curr.key)
                curr = deref(curr.right)
            else:
                break

    def _remove(self, node):
        left = deref(deref(node).left)
        right = deref(deref(node).right)

        # has two children
        if left and right:
            succ = self._find_successor(node)
            deref(node).key = deref(succ).key
            setref(succ, deref(succ).right[0])
        # doesn't have any children
        elif not left and not right:
            setref(node, None)
        # has one child
        else:
            n = deref(node)
            n = n.left if deref(n.left) else n.right
            setref(node, deref(n))

    def _find_successor(self, node):
        n = deref(node).right
        while deref(n).left[0]:
            n = deref(n).left
        return n

    def _find(self, key):
        curr = self.root
        while deref(curr):
            if key < deref(curr).key:
                curr = deref(curr).left
            elif key > deref(curr).key:
                curr = deref(curr).right
            else:
                return curr
        raise KeyError('{0}'.format(key))
