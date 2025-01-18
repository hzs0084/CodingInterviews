'''
TikTok Server Network Optimization

TikTok is growing, and the developers need more servers to keep up with all the new users. 
They have installed n serv ers across different locations, and each server is palced ona  large frid. the ith server is located at the point (x[i], y[i]) on the grid.

The cost of conneting two servers, i and j, is the smaller of the two differences:
    - The difference in the x-coordinates, |x[i] - x[j]|.
    - The difference in the y-coordinates, |y[i] - y[j]|.

Here, |a| means the absolute value of the number a (ignoring any negative signs).

Your task is to find the minimum cost to build a network where all the servers can communicate with each other, either directly or through other servers.

Example:

n = 3
x = [2,4,8]
y = [6,10,9]

To connect the servers, here's the strategy:

1. Connect the first and second servers: The servers are at (2,6) and (4,10). The cost is min(|2-4|, |6-10|) = 2.

2. Connect the second and third servers: The servers are at (4,10) and (8,9). The cost is min(|4-8|, |10-9|) = 1.

3. Connect the first and third servers: The servers are at (2,6) and (8,9). The cost is min(|2-8|, |6-9|) = 3.

So, the optimal way is to connet the first and second servers for 2, and then the second and third servers for 1. Thus, the total minimum cost is 2 + 1 = 3.
'''

import math
import os
import random
import re
import sys



#
# Complete the 'getMinTikTokServerNetworkCost' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY x
#  2. INTEGER_ARRAY y
#

import heapq

def getMinTikTokServerNetworkCost(x, y):
    n = len(x)
    edges = []
    
    # Construct edges for the MST
    for i in range(n):
        for j in range(i + 1, n):
            cost = min(abs(x[i] - x[j]), abs(y[i] - y[j]))
            edges.append((cost, i, j))
    
    # Sort edges by cost
    edges.sort()
    
    # Union-Find for Kruskal's algorithm
    parent = list(range(n))
    rank = [0] * n
    
    def find(u):
        if parent[u] != u:
            parent[u] = find(parent[u])
        return parent[u]
    
    def union(u, v):
        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            if rank[root_u] > rank[root_v]:
                parent[root_v] = root_u
            elif rank[root_u] < rank[root_v]:
                parent[root_u] = root_v
            else:
                parent[root_v] = root_u
                rank[root_u] += 1
    
    # Kruskal's algorithm
    mst_cost = 0
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += cost
    
    return mst_cost

if __name__ == '__main__':
    x = [4, 3, 2, 1]
    y = [4, 3, 2, 1]
    print(getMinTikTokServerNetworkCost(x, y))


# Optimized Solution

# import heapq

# def getMinTikTokServerNetworkCost(x, y):
#     n = len(x)
#     points = [(x[i], y[i], i) for i in range(n)]
#     edges = []

#     # Sort points by x-coordinates and add edges
#     points.sort(key=lambda p: p[0])
#     for i in range(n - 1):
#         cost = min(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
#         edges.append((cost, points[i][2], points[i + 1][2]))

#     # Sort points by y-coordinates and add edges
#     points.sort(key=lambda p: p[1])
#     for i in range(n - 1):
#         cost = min(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
#         edges.append((cost, points[i][2], points[i + 1][2]))

#     # Kruskal's algorithm using Union-Find
#     parent = list(range(n))
#     rank = [0] * n

#     def find(u):
#         if parent[u] != u:
#             parent[u] = find(parent[u])
#         return parent[u]

#     def union(u, v):
#         root_u = find(u)
#         root_v = find(v)
#         if root_u != root_v:
#             if rank[root_u] > rank[root_v]:
#                 parent[root_v] = root_u
#             elif rank[root_u] < rank[root_v]:
#                 parent[root_u] = root_v
#             else:
#                 parent[root_v] = root_u
#                 rank[root_u] += 1

#     # Sort edges by cost
#     edges.sort()
#     mst_cost = 0

#     # Process edges
#     for cost, u, v in edges:
#         if find(u) != find(v):
#             union(u, v)
#             mst_cost += cost

#     return mst_cost

import heapq

def getMinTikTokServerNetworkCost(x, y):
    n = len(x)
    points = [(x[i], y[i], i) for i in range(n)]
    edges = []

    # Generate edges based on sorted x-coordinates
    points.sort(key=lambda p: p[0])
    for i in range(n - 1):
        cost = min(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
        edges.append((cost, points[i][2], points[i + 1][2]))

    # Generate edges based on sorted y-coordinates
    points.sort(key=lambda p: p[1])
    for i in range(n - 1):
        cost = min(abs(points[i][0] - points[i + 1][0]), abs(points[i][1] - points[i + 1][1]))
        edges.append((cost, points[i][2], points[i + 1][2]))

    # Initialize Union-Find structures
    parent = list(range(n))
    rank = [0] * n

    def find(node):
        """Find the root of a node with path compression."""
        if parent[node] != node:
            parent[node] = find(parent[node])
        return parent[node]

    def union(node1, node2):
        """Union two sets by rank."""
        root1 = find(node1)
        root2 = find(node2)
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root2] = root1
                rank[root1] += 1

    # Sort edges by cost
    edges.sort()
    mst_cost = 0

    # Construct the Minimum Spanning Tree (MST)
    for cost, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst_cost += cost

    return mst_cost
