#graph of n nodes, labelled from 0 to n-1
# given an integer n and a list of edges where edges[i] = [ai,bi] (edge is a list of the two nodes the edge connects)
#return true if the edges of the given graph make up a valid tree and false otherwise

#what's a valid tree?
    # n nodes, n-1 edges, all nodes connected

# n = 5 (nodes: 0,1,2,3,4)
# edges [[0,1][1,2],[2,3],[3,4],[4,1]]

class Solution:
    def isValidTree(self, n: int, List[List[int]]) -> bool:
        #check that there aren't more edges than nodes
        # and that its not disconnected
        if len(edges) != n-1:
            return False
        #check that there are no cycles (graph traversal)
        #create adjacency list
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()

        queue = [0]
        visited.add(0)

        while(queue):
            node = queue.pop()
            for neighbor in adj[node]:
                if neighbor not in visited:
                    #process
                    visited.add(neighbor)
                    queue.append(neighbor)
        return len(visited) == n
                #follow the edges
        # if I ever encounter a node I already visited, return False
        # else return True


