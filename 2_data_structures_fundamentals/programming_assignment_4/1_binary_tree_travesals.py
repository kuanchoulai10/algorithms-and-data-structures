# Uses python3
# Task: You are given a rooted binary tree. Build and output its in-order, pre-order and post-order traversals.
import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size


class Node:
    def __init__(self, key, left, right):
        self.key = int(key)
        # the index of the left child
        self.left = int(left)
        # the index of teh right child
        self.right = int(right)


class TreeOrders:
    def __init__(self):
        self.in_rslt = []
        self.pre_rslt = []
        self.post_rslt = []

    def read(self):
        self.n = int(sys.stdin.readline())
        self.nodes = [Node(*sys.stdin.readline().split()) for _ in range(self.n)]

    def in_order(self, idx):
        node = self.nodes[idx]
        # 左節點
        if (node.left != -1):
            self.in_order(node.left)
        # 當前節點
        self.in_rslt.append(node.key)
        # 右節點
        if (node.right != -1):
            self.in_order(node.right)
        return self.in_rslt

    def pre_order(self, idx):
        node = self.nodes[idx]
        # 當前節點
        self.pre_rslt.append(node.key)
        # 左節點
        if (node.left != -1):
            self.pre_order(node.left)
        # 右節點
        if (node.right != -1):
            self.pre_order(node.right)
        return self.pre_rslt

    def post_order(self, idx):
        node = self.nodes[idx]
        # 左節點
        if (node.left != -1):
            self.post_order(node.left)
        # 右節點
        if (node.right != -1):
            self.post_order(node.right)
        # 當前節點
        self.post_rslt.append(node.key)
        return self.post_rslt


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.in_order(idx=0)))
    print(" ".join(str(x) for x in tree.pre_order(idx=0)))
    print(" ".join(str(x) for x in tree.post_order(idx=0)))

threading.Thread(target=main).start()
