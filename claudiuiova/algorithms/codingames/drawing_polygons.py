"""You have to print the direction (CLOCKWISE or COUNTERCLOCKWISE) used to construct a polygon defined by a
specified sequence of points.

Consider that the points represent the vertices of an arbitrary polygon, and you can draw the polygon if you take the
points pairwise, in the order they are given. So, every two consecutive points form an edge, and the last edge is
formed by the last and the first points.

Sample 1

P(1) => x=6, y=5
P(2) => x=11, y=5
P(3) => x=11, y=2
P(4) => x=3, y=2

│ · · · · · · · · · · · · ·
│ · · · · · 1 · · · · 2 · ·
│ · · · · · · · · · · · · ·
│ · · · · · · · · · · · · ·
│ · · 4 · · · · · · · 3 · ·
│ · · · · · · · · · · · · ·
┼───────────────────────────

The polygon is in the CLOCKWISE direction.

Sample 2

P(1) => x=6, y=5
P(2) => x=11, y=5
P(3) => x=11, y=2
P(4) => x=16, y=7

│ · · · · · · · · · · · · · · · · · ·
│ · · · · · · · · · · · · · · · 4 · ·
│ · · · · · · · · · · · · · · · · · ·
│ · · · · · 1 · · · · 2 · · · · · · ·
│ · · · · · · · · · · · · · · · · · ·
│ · · · · · · · · · · · · · · · · · ·
│ · · · · · · · · · · 3 · · · · · · ·
│ · · · · · · · · · · · · · · · · · ·
┼─────────────────────────────────────

The polygon is in the COUNTERCLOCKWISE direction."""

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# n = int(input())
points = [(6, 5), (11, 5), (11, 2), (3, 2)]
# for i in range(n):
#     x, y = [int(j) for j in input().split()]
#     points.append((x, y))


def get_edge_points_sum(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return (x2 - x1) * (y2 + y1)


def check_if_clockwise(points):
    p1, p2, p3, p4 = points

    v1 = get_edge_points_sum(p1, p2)
    v2 = get_edge_points_sum(p2, p3)
    v3 = get_edge_points_sum(p3, p4  )
    v4 = get_edge_points_sum(p4, p1)

    return sum([v1, v2, v3, v4])

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


print(check_if_clockwise(points))
# print("CLOCKWISE")
