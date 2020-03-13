#Uses python3
import sys
from itertools import combinations
from math import sqrt

def kruskal(x,y):
    n = len(x)
    pairs_v = list(combinations(range(n), 2))
    dist = 0
    # create edges by dictionary
    edges = {}
    for v1,v2 in pairs_v:
        x_squared_diff = (x[v1]-x[v2])**2
        y_squared_diff = (y[v1]-y[v2])**2
        edges[v1,v2] = x_squared_diff + y_squared_diff
    # sort edges by squared difference 
    sorted_edges = sorted(edges.items(), key = lambda x: x[1], reverse = True)
    # create a disjoint set
    disjoint_set = {}
    for i in range(n):
        disjoint_set[i] = set([i])
    # greedy algorithm
    while sorted_edges:
        (v1, v2), squared_d = sorted_edges.pop()
        if disjoint_set[v1] != disjoint_set[v2]:
            cc = set.union(disjoint_set[v1], disjoint_set[v2])
            update_dict = dict(zip(list(cc), [cc] * len(cc)))
            disjoint_set.update(update_dict)
            # cc = set.union(disjoint_set[v1], disjoint_set[v2])
            # for v in list(cc):
            #     disjoint_set[v] = cc
            dist += sqrt(squared_d)
    return dist


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(kruskal(x, y)))
