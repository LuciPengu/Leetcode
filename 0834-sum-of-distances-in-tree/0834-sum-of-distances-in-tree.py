from typing import List
from collections import defaultdict, deque

class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]  # Only one node, no distances to sum.
        
        # Graph to store the tree
        tree = defaultdict(list)
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)

        # Arrays to store subtree sizes and results
        count = [1] * n  # subtree size (default to 1 for each node itself)
        res = [0] * n  # result array to store sum of distances

        # Postorder: compute subtree sizes and initial sum of distances
        def postorder(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                postorder(child, node)
                count[node] += count[child]
                res[node] += res[child] + count[child]
        
        # Preorder: calculate distances for all nodes based on root distances
        def preorder(node, parent):
            for child in tree[node]:
                if child == parent:
                    continue
                res[child] = res[node] - count[child] + (n - count[child])
                preorder(child, node)

        # Start the postorder and preorder traversal from node 0
        postorder(0, -1)
        preorder(0, -1)

        return res
