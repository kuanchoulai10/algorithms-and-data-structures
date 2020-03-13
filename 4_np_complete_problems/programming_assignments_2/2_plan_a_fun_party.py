#uses python3

import sys
import threading

# This code is used to avoid stack overflow issues
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**26)  # new thread will get stack of such size

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.neighbors = []

def read_graph():
    size = int(input())
    graph = [Vertex(w) for w in map(int, input().split())]
    for _ in range(1, size):
        a, b = list(map(int, input().split()))
        graph[a-1].neighbors.append(b-1)
        graph[b-1].neighbors.append(a-1)
    return graph

def max_w_ind_set(graph, v, prev):
    if len(graph) >= 3:
        global DP_weights
        if DP_weights[v] == 0: # updating 'DP_weights[v]' if needed
            V = graph[v]
            children = [n for n in V.neighbors if n != prev]
            # condition 1: Vertex v is a leaf.(has no child)
            if len(children) <= 0:
                DP_weights[v] = V.weight
            # condition 2: Vertex v isn't a leaf
            else:
                # alternative 1: Vertex v and its grandchildren
                w1 = V.weight
                for c in children:
                    grandchildren = [n for n in graph[c].neighbors if n != v]
                    for i in range(len(grandchildren)):
                        gc = grandchildren[i]
                        w1 += max_w_ind_set(graph, gc, c)
                # alternative 2: Vertex v's child
                w2 = 0
                for c in children:
                    w2 += max_w_ind_set(graph, c, v)
                # choose the bigger one between w1 and w2
                DP_weights[v] = max(w1, w2)
        return DP_weights[v]
    else:
        return graph[0].weight if len(graph)==1 else max(graph[0].weight, graph[1].weight)

graph = read_graph()
DP_weights = [0] * len(graph)
def main():
    weight = max_w_ind_set(graph, 0, -1)
    print(weight)

# This is to avoid stack overflow issues
threading.Thread(target=main).start()

