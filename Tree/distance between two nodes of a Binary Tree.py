"""
Find the distance between two keys in a binary tree, no parent pointers are given.
Distance between two nodes is the minimum number of edges to be traversed to reach one node from other.

Dist(n1, n2) = Dist(root, n1) + Dist(root, n2) - 2*Dist(root, lca)

"""

class TreeClass(object):
    def __init__(self, val):
        self.node = val
        self.left = None
        self.right = None

class Solution:
    def