# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

def print_equisatisfiable_sat_formula():
    def nCr(n,r):
        from math import factorial
        f = factorial
        return f(n) // f(r) // f(n-r)
    from itertools import combinations

    if n==1:
        print('1 1')
        print('1 -1 0')
    elif len(edges) == 0:
        print('2 1')
        print('1 0')
        print('-1 0')
    else:
        set_all = set(list(combinations(range(1, n+1), 2)))
        set_edges = set()
        set_edges.update([(v2,v1) if v1>v2 else (v1,v2) for v1,v2 in edges])
        set_diff = set_all - set_edges

        # print out the number of clauses in the formula 
        #     and the number of variables respectively
        num_C = (n+nCr(n,2)*n) * 2 + (n-1)*len(set_diff)*2
        num_V = n**2
        print('%i %i' % (num_C, num_V))
        # region create_dict
        d = {}
        for v in range(1, n+1):
            d[v] = {}
            for pos in range(1, n+1):
                d[v][pos]= v*n - (n-pos)
        # endregion create_dict
        # region vertex
        #     1. each vertex belongs to a path
        for v in range(1, n+1):
            positions = d[v].values()
            s = ''
            for pos in positions:
                s += '%i ' % pos
            s += '0'
            print(s)
        #     2. each vertex appears just once in a path
        for v in range(1, n+1):
            positions = d[v].values()
            for v1,v2 in list(combinations(positions, 2)):
                print('%i %i 0' % (-v1, -v2))
        # endregion position
        # region position
        #     3. each position in a path is occupied by some vertex
        for pos in range(1, n+1):
            s = ''
            for v in range(1, n+1):
                s += '%i ' % d[v][pos]
            s += '0'
            print(s)
        #     4. no two vertices occupy the same position of a path
        for pos in range(1, n+1):
            vertices = []
            for v in range(1, n+1):
                vertices.append(d[v][pos])
            for v1, v2 in list(combinations(vertices, 2)):
                print('%i %i 0' % (-v1, -v2))
        # endregion position
        # region edges
        #     5. two nonadjacent vertices cannot be adjacent in the path.
        while set_diff:
            v1,v2 = set_diff.pop()
            for pos in range(1,n):
                var1 = d[v1][pos]
                var2 = d[v2][pos+1]
                print('%i %i 0' % (-var1, -var2))
                var1_rev = d[v2][pos]
                var2_rev = d[v1][pos+1]
                print('%i %i 0' % (-var1_rev, -var2_rev))
        # endregion edges

print_equisatisfiable_sat_formula()