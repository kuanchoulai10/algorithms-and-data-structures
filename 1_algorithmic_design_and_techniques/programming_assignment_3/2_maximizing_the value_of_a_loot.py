# Uses python3
import sys

def get_optimal_value(capacity, values, weights):
    """
    Task: The goal of this code problem is to implement an algorithm for the fractional knapask problem.
    """
    # calculate the price per unit of each item
    price_per_units = [v/w for v,w in zip(values, weights)]
    
    # sort values and weights by price per unit in descending order
    # sorted_result = [(price_per_unit, value, weight), ...]
    sorted_result = sorted(zip(price_per_units, values, weights), reverse=True)
    
    # greedy alg.
    total_value = 0
    for price_per_unit, _, weight in sorted_result:
        if capacity==0:
            return total_value
        # decide how much amount we're gonna take and multiply it by price_per_unit
        amount = min(weight, capacity)
        total_value += price_per_unit * amount
        capacity -= amount
    
    return total_value    
if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    # n: the number of items
    # capacity: the capacity of a knapask
    # values: values of the items
    # weights: weights of the items
    n, capacity = data[:2]
    values = data[2:(2*n+2):2]
    weights = data[3:(2*n+2):2]
    # find the maximal value of fractions of items that fit into the knapask.
    opt_value = get_optimal_value(capacity, values, weights)
    print("{:.4f}".format(opt_value))