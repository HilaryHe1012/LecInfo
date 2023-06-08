##
# 1. Update shortest path
# - decrease key operation
# 2. Find the next node (O(V)) if we exhaust all V nodes 
# Thus complexity is O(2.V + 1.E)
# if we were to use a dictionary to keep track of the shortest path we get O(V^2+E)
# Same for a list.
# 
# Min heap - O(vlogV+ ElogV) 
# - we can find the next node in constant time, however, we need to delete that node for the node to make sense thus log V
# - decrease key in min heap is log V.
# - Is this better than O(V^2+E)? Sometimes, it depends on the graph, depends on the ratio between V and E 
# -- if V is super super dense then min heap, if it is sparse, use dict
# 
# As it turns out, the fibnacci heap leads to O(VlogV + E), they can do 
# decrease key in constant time. And they can't do extract min/max in constant time

import min_heap

def dijkstra(G, s, d):
    marked, dist = {}, {}
    Q = min_heap.MinHeap([])
    # initializing values
    for i in range(G.number_of_nodes()):
        marked[i] = False
        dist[i] = float("inf")
        Q.insert_elements(min_heap.Element(i, float("inf")))
    # start node
    Q.decrease_key(s, 0)
    dist[s] = 0

    while not (Q.is_empty() or marked[d]):
        current_node = Q.extract_min().value 
        marked[current_node] = True 
        for neighbour in G.adj[current_node]:
            edge_weight = G.w[(current_node, neighbour)]
            if not marked[neighbour]:
                if dist[current_node] + edge_weight < dist[neighbour]:
                    dist[neighbout] = dist[currrent_node] + edge_weight 
                    Q.decrease_key(neighbour, dist[neighbour])
    return dist[d]