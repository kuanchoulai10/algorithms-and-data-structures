# Uses python3
import sys
import threading

class Node():
    def __init__(self):
        self.children = []

    def add_child(self, node):
        self.children.append(node)

def compute_height(node):
    """
    給定一個節點，計算「當前節點當作root」的情況下的高度為何
    """
    # 初始化當前樹狀結構高度為 1 
    height = 1
    # 如果沒有子節點，則回傳當前高度: 1
    if not len(node.children):
        return height
    # 如果有子節點，則分別計算「子節點當作root」的情況下的高度為何，取其大
    # 接著加上原本的 1 ，則為「當前節點當作root」的情況下的高度
    height += max([compute_height(child_node) for child_node in node.children])

    return height

def main():
    """
    Task: You are given a description of a rooted tree. Your task is to compute and output its height. Recall
        that the height of a (rooted) tree is the maximum depth of a node, or the maximum distance from a
        leaf to the root. You are given an arbitrary tree, not necessarily a binary tree.
    Input Format: The first line contains the number of nodes n. 
        The second line contains n integer numbers from −1 to n-1 — parents of nodes.
        If the i-th one of them (0 <= i <= n−1) is −1, node i is the root, otherwise it’s 0-based index of the parent of i-th node.
        It is guaranteed that there is exactly one root. It is guaranteed that the input represents a tree.
    Output Format: Output the height of the tree.
    """
    n = int(input())
    parents = list(map(int, input().split()))
    # 建立每個節點類別
    nodes = [Node() for _ in range(n)]
    # 迭代每個節點
    for child_idx in range(n):
        # 找出父節點位置
        parent_idx = parents[child_idx]
        # 如果當前節點是root，則記錄它的位置資訊
        # 如果不是，則對父節點加入「子節點的指標」
        if parent_idx==-1:
            root_node = nodes[child_idx]
        else:
            nodes[parent_idx].add_child(nodes[child_idx])
    # 建立好樹狀結構後，從根節點開始以遞迴計算樹狀結構的高度
    print(compute_height(root_node))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
