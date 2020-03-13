# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple(typename="Segment", field_names=["start","end"])

def optimal_points(segments):
    """
    Task: Given a set of n segments {[a_0, b_0], [a_1, b_1], ..., [a_{n-1}, b_{n-1}]} with integer coordinates on a line, find the minimum
    number m of points such that each segment contains at least one point. That is, find a set of integers X of the minimum size such that
    for any segment [a_i, b_i] there is a point x \isin X such that a_i <= x <= b_i
    """
    # for storing the result
    points = []
    # sort segments by `end` field in ascending order
    segments = sorted(segments, key=lambda seg: seg.end)
    
    # greedy alg.
    while len(segments)>0:
        # find the minimum end point
        min_end_point = segments[0].end
        points.append(min_end_point)
        # remove the segment from `segments` if the minimum end point is in it.
        while True:
            # check if the minimum end point is in the segment
            seg = segments[0]
            if seg.start <= min_end_point <= seg.end:
                segments.pop(0)
            else:
                break
            # break the loop if there is no element in `segments`
            if not len(segments):
                break
    return points

if __name__ == '__main__':
    n, *data = map(int, sys.stdin.read().split())
    # segments = [(start, end), ...]
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
