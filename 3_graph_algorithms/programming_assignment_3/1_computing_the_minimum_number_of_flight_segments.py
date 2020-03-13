#Uses python3

import sys

def breadth_first_search(adj_lst, s):
    from queue import Queue
    Q = Queue()
    global dist_lst
    global prev_lst
    dist_lst[s] = 0
    Q.put(s)
    while not Q.empty():
        u = Q.get()
        for adj in adj_lst[u]:
            if dist_lst[adj] == float('inf'):
                Q.put(adj)
                dist_lst[adj] = dist_lst[u] + 1
                prev_lst[adj] = u

def reconstruct_path(s, t, prev_lst):
    path = []
    while  t != s:
        path.append(t)
        t = prev_lst[t]
        if t == None:
            return []
    path.reverse()
    return path

def distance(adj_lst, s, t):
    breadth_first_search(adj_lst, s)
    global prev_lst
    path = reconstruct_path(s, t, prev_lst)
    if len(path) != 0:
        return len(path)
    else:
        return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj_lst = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_lst[a - 1].append(b - 1)
        adj_lst[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    dist_lst = [float('inf')] * len(adj_lst)
    prev_lst = [None] * len(adj_lst)
    print(distance(adj_lst, s, t))


