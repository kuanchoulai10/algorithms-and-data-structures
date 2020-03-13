#Uses python3

import sys

sys.setrecursionlimit(200000)

def depth_first_search(adj_lst):
    def explore(v, adj_lst):
        nonlocal visited
        nonlocal pre_numbers
        nonlocal post_numbers
        nonlocal count
        visited[v] = True
        pre_numbers[v] = count
        count += 1
        for adj in adj_lst[v]:
            if visited[adj] == False:
                explore(adj, adj_lst)
        post_numbers[v] = count
        count += 1
    visited = [False] * len(adj_lst)
    count = 1
    pre_numbers = [0] * len(adj_lst)
    post_numbers = [0] * len(adj_lst)
    for v in range(len(adj_lst)):
        if visited[v] == False:
            explore(v, adj_lst)
    sorted_post_numbers = list(zip(post_numbers, range(len(adj_lst))))
    sorted_post_numbers.sort(reverse = True)
    order = [val for tup in sorted_post_numbers for val in tup][1::2]
    return order

def number_of_strongly_connected_components(adj_lst, reversed_adj_lst):
    def explore(v, adj_lst):
        nonlocal visited
        nonlocal pre_numbers
        nonlocal post_numbers
        nonlocal count
        visited[v] = True
        pre_numbers[v] = count
        count += 1
        for adj in adj_lst[v]:
            if visited[adj] == False:
                explore(adj, adj_lst)
        post_numbers[v] = count
        count += 1

    visited = [False] * len(adj_lst)
    count = 1
    pre_numbers = [0] * len(adj_lst)
    post_numbers = [0] * len(adj_lst)

    order = depth_first_search(reversed_adj_lst)
    visited = [False] * len(adj_lst)
    count = 1
    pre_numbers = [0] * len(adj_lst)
    post_numbers = [0] * len(adj_lst)
    num_SCC = 0
    for v in order:
        if visited[v] == False:
            explore(v, adj_lst)
            num_SCC += 1
    return num_SCC

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj_lst = [[] for _ in range(n)]
    for (a, b) in edges:
        adj_lst[a - 1].append(b - 1)
    
    reversed_edges = list(zip(data[1:(2 * m):2], data[0:(2 * m):2]))
    reversed_adj_lst = [[] for _ in range(n)]
    for (a, b) in reversed_edges:
        reversed_adj_lst[a - 1].append(b - 1)
    
    print(number_of_strongly_connected_components(adj_lst, reversed_adj_lst))
