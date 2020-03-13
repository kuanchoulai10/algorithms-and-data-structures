#Uses python3

import sys

def depth_first_search(adj_lst):
    def explore(v):
        nonlocal adj_lst
        nonlocal visited
        nonlocal pre_numbers
        nonlocal post_numbers
        nonlocal count
        visited[v] = True
        pre_numbers[v] = count
        count += 1
        for adj in adj_lst[v]:
            if visited[adj] == False:
                explore(adj)
        post_numbers[v] = count
        count += 1
    
    visited = [False] * len(adj_lst)
    count = 1
    pre_numbers = [0] * len(adj_lst)
    post_numbers = [0] * len(adj_lst)
    for v in range(len(adj_lst)):
        if visited[v] == False:
            explore(v)
    return list(zip(post_numbers, range(len(adj_lst))))


def toposort(adj_lst):
    post_numbers = depth_first_search(adj_lst)
    post_numbers.sort(reverse = True)
    order = [val for tup in post_numbers for val in tup][1::2]
    return order

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj_lst = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_lst[a - 1].append(b - 1)
    order = toposort(adj_lst)
    for x in order:
        print(x + 1, end=' ')

