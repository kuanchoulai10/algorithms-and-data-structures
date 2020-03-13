#Uses python3

import sys

def explore(adj_lst, visited, vrtx):
    visited[vrtx] = True
    for adj in adj_lst[vrtx]:
        if visited[adj] == False:
            explore(adj_lst, visited, adj)

def reach(adj_lst, x, y):
    visited = [False] * len(adj_lst)
    explore(adj_lst, visited, x)
    if visited[y] == True:
        return 1
    else:
        return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2] # number of vertices and edges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj_lst = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj_lst[a - 1].append(b - 1)
        adj_lst[b - 1].append(a - 1)
    print(reach(adj_lst, x, y))
