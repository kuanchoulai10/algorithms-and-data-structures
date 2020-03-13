#!/usr/bin/python3
import sys
import threading

sys.setrecursionlimit(10**8)  # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

# Task: You are given a binary tree with integers as its keys. You need to test whether it is a correct binary
#   search tree. The definition of the binary search tree is the following: for any node of the tree, if its
#   key is x, then for any node in its left subtree its key must be strictly less than x, and for any node in
#   its right subtree its key must be strictly greater than x. In other words, smaller elements are to the
#   left, and bigger elements are to the right. You need to check whether the given binary tree structure
#   satisfies this condition. You are guaranteed that the input contains a valid binary tree. That is, it is a
#   tree, and each node has at most two children.


class Node:
    def __init__(self, key, left, right):
        self.key = int(key)
        # the index of the left child
        self.left = int(left)
        # the index of teh right child
        self.right = int(right)


def is_bst(tree):
    """wrapper function"""
    # 如果二元搜尋樹沒有任何一個元素，則回傳True
    if not len(tree):
        return True
    return is_bst_util(tree, 0, -float('inf'), float('inf'))


def is_bst_util(tree, idx, lower, upper):
    """
    檢查當前節點(`tree[idx]`)是否在(lower, upper)的範圍內
    """
    node = tree[idx]
    # 如果當前節點不在(lower, upper)的範圍內，代表它不滿足二元搜尋樹的規定，因此回傳False
    if (node.key<=lower) or (node.key>=upper):
        return False
    # 如果當前節點在(lower, upper)的範圍內，則檢查
    # - 左節點是否處在(lower, node.key)的範圍內
    # - 右節點是否處在(node.key, upper)的範圍內
    rslt = (
        (is_bst_util(tree, node.left, lower, node.key) if (node.left!=-1) else True) and
        (is_bst_util(tree, node.right, node.key-1, upper) if (node.right!=-1) else True)
    )
    return rslt


def main():
    n = int(sys.stdin.readline().strip())
    tree = [Node(*sys.stdin.readline().split()) for _ in range(n)]
    print('CORRECT' if is_bst(tree) else 'INCORRECT')


threading.Thread(target=main).start()

# reference: https://www.geeksforgeeks.org/a-program-to-check-if-a-binary-tree-is-bst-or-not/