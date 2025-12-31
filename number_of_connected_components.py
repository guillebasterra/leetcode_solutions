# number of connected components in an undirected graph
# graph of n nodes
# given an integer n and an array edges where edges[i] = [ai,bi] (edge between nodes)
# return the number of connected components in the graph
from typing import List
class Solution:
    def countComponents(self,n:int,edges: List[List[int]]) -> int:
        if n == 0 or n==1: return n
        num_connected_components = 0
        adj = {i:[] for i in range(n)}
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        #now have an adjacency list connecting all the nodes
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        for i in range(n):
            if i not in visited:
                num_connected_components += 1
                dfs(i)
        return num_connected_components


if __name__ == "__main__":
    sol = Solution()

    # Test Case 1
    n1 = 5
    edges1 = [[0,1], [1,2], [3,4]]
    print(f"Test Case 1: {sol.countComponents(n1, edges1)}") 
    # Expected Output: 2

    # Test Case 2
    n2 = 5
    edges2 = [[0,1], [1,2], [2,3], [3,4]]
    print(f"Test Case 2: {sol.countComponents(n2, edges2)}") 
    # Expected Output: 1
    
    # Test Case 3 (Empty edges, 5 isolated nodes)
    n3 = 5
    edges3 = []
    print(f"Test Case 3: {sol.countComponents(n3, edges3)}")
    # Expected Output: 5



