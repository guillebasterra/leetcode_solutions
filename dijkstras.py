def dijkstra(edges,n,src):
    adj = collections.defaultDict(list)
    for s,d,w in edges:
        adj[s].append((d,w))

    shortest = {}
    minHeap = [(0,src)]

    while minHeap:
        w1,n1 = heapq.heappop(minheap)
        if n1 in shortest:
            continue
        shortest[n1] = w1

        for n2,w2 in adj[n1]:
            if n2 not in shortest:
                heapq.heappush(minheap, (w1+w2,n2))
    return shortest

