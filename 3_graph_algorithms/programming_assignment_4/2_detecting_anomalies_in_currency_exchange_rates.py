#Uses python3

import sys

def negative_cycle(adj_lst, cost_lst):
    def reconstruct_negative_cycle(v, prev_lst):
        # iterate (finding previous vertex) 'n' times so that the vertex will 
        #     be definitely on the negative cycle path
        for _ in range(n):
            v = prev_lst[v]
        # set the vertex as a starting vertex in the cycle,
        #     then find previous vertex until we find starting vertex 
        start_v = v
        negative_cycle = [start_v]
        while start_v != prev_lst[v]:
            v = prev_lst[v]
            negative_cycle.append(v)
        negative_cycle.reverse()
        return negative_cycle
    # initialize all the variables we need
    n = len(adj_lst)
    dist_lst = [float('inf')] * n
    prev_lst = [None] * n
    dist_lst[0] = 0
    # iterate Bellman-Ford algorithm 'n' times
    for t in range(1, n+1):
        num_update = 0
        # in each iteration, go through every vertex to relax all the edges 
        for v in range(n):
            for i, adj in enumerate(adj_lst[v]):
                # relax all the edges
                if dist_lst[v] + cost_lst[v][i] < dist_lst[adj]:
                    num_update += 1
                    dist_lst[adj] = dist_lst[v] + cost_lst[v][i]
                    prev_lst[adj] = v
                    # there is a negative cycle in the graph if we could update 
                    #     the distance value at iteration round 'n'
                    if t == n:
                        # # reconstruct the negative cycle path
                        # cycle = reconstruct_negative_cycle(adj, prev_lst)
                        # print(cycle) 
                        return 1
        if (num_update == 0):
            return 0
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj_lst = [[] for _ in range(n)]
    cost_lst = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj_lst[a - 1].append(b - 1)
        cost_lst[a - 1].append(w)
    print(negative_cycle(adj_lst, cost_lst))

