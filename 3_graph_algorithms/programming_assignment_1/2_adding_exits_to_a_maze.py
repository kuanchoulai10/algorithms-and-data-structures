#Uses python3

import sys

def explore(adj_lst, visited, vrtx):
    visited[vrtx] = True
    for adj in adj_lst[vrtx]:
        if visited[adj] == False:
            explore(adj_lst, visited, adj)

def depth_first_search(adj_lst):
    visited = [False] * len(adj_lst)
    cc = 0
    for v in range(len(adj_lst)):
        if visited[v] == False:
            explore(adj_lst, visited, v)
            cc += 1
    return cc

def number_of_components(adj_lst):
    result = depth_first_search(adj_lst)
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2] # number of vertices and edges
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj_lst = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_lst[a - 1].append(b - 1)
        adj_lst[b - 1].append(a - 1)
    print(number_of_components(adj_lst))

