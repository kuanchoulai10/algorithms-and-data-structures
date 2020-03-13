#Uses python3

import sys

def bipartite(adj_lst):
    from queue import Queue
    Q = Queue()
    dist_lst = [float('inf')] * len(adj_lst)
    dist_lst[0] = 0
    Q.put(0)
    while not Q.empty():
        u = Q.get()
        for adj in adj_lst[u]:
            if dist_lst[adj] == float('inf'):
                Q.put(adj)
                dist_lst[adj] = dist_lst[u] + 1
            else:
                if (dist_lst[adj] % 2) == (dist_lst[u] % 2):
                    return 0
    return 1

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
    print(bipartite(adj_lst))
