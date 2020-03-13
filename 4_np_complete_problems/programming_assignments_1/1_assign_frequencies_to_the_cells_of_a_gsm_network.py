# python3
n, m = map(int, input().split())
edges = [ list(map(int, input().split())) for i in range(m) ]

# This solution prints a simple satisfiable formula
# and passes about half of the tests.
# Change this function to solve the problem.
def print_equisatisfiable_sat_formula():
    num_C = n*4+m*3
    num_V = n*3
    print('%i %i' % (num_C, num_V))
    for v in range(1, n+1):
        r = 3*v-2
        g = 3*v-1
        b = 3*v 
        print('%i %i %i 0' % (r,g,b))
        print('%i %i 0' % (-r,-g))
        print('%i %i 0' % (-g,-b))
        print('%i %i 0' % (-r,-b))

    for u,v in edges:
        u_r = 3*u-2
        u_g = 3*u-1
        u_b = 3*u
        v_r = 3*v-2
        v_g = 3*v-1
        v_b = 3*v
        print('%i %i 0' % (-u_r,-v_r))
        print('%i %i 0' % (-u_g,-v_g))
        print('%i %i 0' % (-u_b,-v_b))

print_equisatisfiable_sat_formula()
