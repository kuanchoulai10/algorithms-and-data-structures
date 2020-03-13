# Uses python3
import sys
import threading

def compute_height(n, parents):
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
    height = 0 
    lvs = [0] * n
    # 遍歷每個節點
    for node, parent in enumerate(parents):
        # 初始當前節點、當前節點的父節點、當前層級
        curr_node = node
        curr_parent = parent
        lv = 1
        # 執行「直到找到root為止」的任務
        while curr_parent!=-1:
            # 如果當前節點的「父節點」已經計算過層級，則直接更新當前節點的層級並跳出
            if lvs[curr_parent]>0:
                lv += lvs[curr_parent]
                break
            # 如果當前節點的「父節點」還沒計算過層級，則更新當前節點的資訊至上一層，即「父節點」
            else:
                curr_node = curr_parent
                curr_parent = parents[curr_node]
                lv += 1
        # 紀錄從 root 到原本節點 (`node`) 是隔幾個層級並追蹤該樹狀結構的高度
        lvs[node] = lv
        height = max(height, lv)
    return height

def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
