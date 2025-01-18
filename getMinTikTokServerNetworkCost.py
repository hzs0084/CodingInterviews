#!/bin/python3

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
