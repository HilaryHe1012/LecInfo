from collections import deque
#from tqdm import tqdm

class Graph:

    def __init__(self, n):
        self.adj = {}
        for i in range(n):
            self.adj[i] = []

    def has_edge(self, node1, node2):
        return node2 in self.adj[node1]

    def add_edge(self, node1, node2):
        # undirected graph
        if not self.has_edge(node1, node2):
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
    
    def get_size(self):
        return len(self.adj)

# finding a smallest vertice coverage problem -> cover all of edges with the minimum amount of vertices
# find if any of the set in the power set is a vetex cover
def is_vertex_cover(G, cover):
    for start in G.adj,keys():
        for end in G.adj[start]:
            # find an edge which is not covered
            if not (start in cover or end in cover):
                return False
    return True                

# minimum vertex cover
# Approximations: max degree, totally random, random edge and other approximations
# O(2^n)
# NP complete problem
def MVC(G):
    nodes = [i for i in range(G.get_size())]
    subsets = get_power_set(nodes)
    min_cover = nodes
    for subset in subsets:
        if is_vertex_cover(G, subset):
            if len(subset) < len(nodes):
                min_cover = subset
    return min_cover


# use a queue
def BFS(G, node1, node2):
    Q = deque([node1])
    marked = {node1 : True}
    for node in G.adj:
        if node != node1:
            marked[node] = False
    while len(Q) != 0:
        current_node = Q.popleft()
        for node in G.adj[current_node]:
            if node == node2:
                return True
            if not marked[node]:
                Q.append(node)
                marked[node] = True
    return False

# use a stack
def DFS(G, node1, node2):
    s = [node1]
    marked = {}
    for node in G.adj:
        marked[node] = False
    while len(S) != 0:
        current_node = S.pop()
        if not marked[current_node]:
            print("Visiting node: " + str(current_node))
            marked[current_node] = True
            for node in G.adj[current_node]:
                if node == node2:
                    return True
                S.append(node)
    return False

# input ([[],[1]],2) -> output [[2],[1,2]]
def add_to_each(subsets, element):
    my_subsets = subsets.copy()
    for subset in my_subsets:
        subset.append(element)
    return my_subsets

def get_power_set(L):
    if L == []: return [[]]
    return get_power_set(L[1:]) + add_to_each(get_power_set(L[1:]), L[0])

G1 = Graph(10)
G1.add_edge(0,1)
G1.add_edge(0,4)
G1.add_edge(0,7)
G1.add_edge(1,2)
G1.add_edge(2,3)
G1.add_edge(4,5)
G1.add_edge(5,6)
G1,add_edge(7,8)
G1.add_edge(8,9)
G1.add_edge(5,9)
G1.add_edge(4,3)