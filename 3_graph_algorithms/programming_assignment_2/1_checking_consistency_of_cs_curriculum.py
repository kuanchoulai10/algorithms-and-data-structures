#Uses python3

import sys

def acyclic(adj_lst):
    def is_cyclic(v):
        nonlocal adj_lst
        nonlocal visited
        nonlocal rec_stack
        visited[v] = True
        rec_stack[v] = True
        for adj in adj_lst[v]:
            if visited[adj] == False:
                if is_cyclic(adj) == True:
                    return True
            elif rec_stack[adj] == True:
                return True
        rec_stack[v]  = False
        return False
    
    visited = [False] * len(adj_lst)
    rec_stack = [False] * len(adj_lst)
    for v in range(len(adj_lst)):
        if visited[v] == False:
            if is_cyclic(v) == True:
                return True
    return False

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj_lst = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_lst[a - 1].append(b - 1)
    print(acyclic(adj_lst))
