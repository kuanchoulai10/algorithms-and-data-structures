#Uses python3

import sys

def dijkstra(adj_lst, cost_lst, start_vertex, end_vertex):
    import heapq as hq
    from itertools import count
    # region p_queue basic operation
    p_queue = []                            # list of entries arranged in a heap
    track_dict = {}                         # mapping of vertices to entries
    REMOVED = 'removed_vertex'              # placeholder for a removed vertex
    counter = count()
    def push_vertex(dist, v):
        # 'Add a new vertex or update the distance of an existing vertex'
        nonlocal p_queue
        nonlocal track_dict
        nonlocal REMOVED
        nonlocal counter
        if v in track_dict: 
            remove_vertex(v)
        count = next(counter)
        entry = [dist, count, v]
        track_dict[v] = entry
        hq.heappush(p_queue, entry)
    def remove_vertex(v):
        # 'Mark an existing vertex as REMOVED. Raise KeyError if not found.'
        nonlocal track_dict
        nonlocal REMOVED
        nonlocal p_queue
        entry = track_dict.pop(v)
        entry[-1] = REMOVED
    def pop_vertex():
        # 'Remove and return the lowest distance vertex. Raise KeyError if empty.'
        nonlocal p_queue
        nonlocal track_dict
        nonlocal REMOVED
        while p_queue:
            dist, count, v = hq.heappop(p_queue)
            if v is not REMOVED:
                del track_dict[v]
                return dist, v
        raise KeyError('pop from an empty priority queue')
    # endregion p_queue basic operation
    dist_lst = [float("inf")] * len(adj_lst)
    prev_lst = [None] * len(adj_lst) 
    dist_lst[start_vertex] = 0
    for v, dist in enumerate(dist_lst):
        push_vertex(dist, v)
    while p_queue:
        dist, v = pop_vertex()
        if v != end_vertex:
            for i, adj in enumerate(adj_lst[v]):
                if (dist_lst[v] + cost_lst[v][i]) < dist_lst[adj]:
                    dist_lst[adj] = (dist_lst[v] + cost_lst[v][i])
                    prev_lst[adj] = v
                    push_vertex(dist_lst[adj], adj)
        else:
            if dist == float('inf'):
                return -1
            #region reconstruct path
            path = []
            path.append(end_vertex)
            prev_v = prev_lst[end_vertex]
            while prev_v != start_vertex:
                path.append(prev_v)
                prev_v = prev_lst[prev_v]
            path.append(start_vertex)
            path.reverse()
            path = [x+1 for x in path]
            print('path =', path)
            #endregion reconstruct path
            return dist
    return -1

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
    start_vertex, end_vertex = data[0] - 1, data[1] - 1
    print(dijkstra(adj_lst, cost_lst, start_vertex, end_vertex))

