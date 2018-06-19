# Question 3
# Given an undirected graph G, find the minimum spanning tree within G. A
# minimum spanning tree connects all vertices in a graph with the smallest
# possible total weight of edges. Your function should take in and return an
# adjacency list structured like this:
#   {'A': [('B', 2)],
#   'B': [('A', 2), ('C', 5)],
#   'C': [('B', 5)]}
# Vertices are represented as unique strings. The function definition should be question3(G)


# Referenced https://www.geeksforgeeks.org for Kruskals refresher
# Greedy Algorithm
from collections import defaultdict

# Global variables
temp = {}
newG = {}
u = None
v = None
w = None
graph = []

# A utility function to find set of an element i
# (uses path compression technique)
def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


# A function that does union of two sets of x and y
# (uses union by rank)
def union(parent, rank, x, y):
    xroot = find(parent, x)
    yroot = find(parent, y)

    # Attach smaller rank tree under root of
    # high rank tree (Union by Rank)
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    # If ranks are same, then make one as root
    # and increment its rank by one
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


# The main function to construct MST using Kruskal's algorithm
def KruskalMST(graph, V, newG):
    # This will store the resultant MST
    result = []  
    results = {}

    i = 0  # An index variable, used for sorted edges
    e = 0  # An index variable, used for result[]

    # Step 1:  Sort all the edges in non-decreasing order of their
    # weight.  If we are not allowed to change the given graph, we
    # can create a copy of graph
    graph = sorted(graph, key=lambda item: item[2])

    parent = []; rank = []

    # Create V subsets with single elements
    for node in range(V):
        parent.append(node)
        rank.append(0)

    # Number of edges to be taken is equal to V-1
    while e < V - 1:

        # Step 2: Pick the smallest edge and increment the index
        # for next iteration
        u, v, w = graph[i]
        i = i + 1
        x = find(parent, u)
        y = find(parent, v)

        # If including this edge does't cause cycle, include it
        # in result and increment the index of result for next edge
        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
        # Else discard the edge

    # Print the contents of result{} to display the built MST
    for u, v, w in result:
        content = []
        content = [(newG[v], w)]
        if newG[u] not in results:
            results[newG[u]] = content
        else:
            results[newG[u]] = results[newG[u]].append(content)
    # Return the results
    return results


def question3(G):
    counter = 0
    # Base case: Empty Dict List
    if G == {}:
        return "List is empty. Try again"
    # Base case: Wrong input type
    if type(G) != dict:
        return "Not a dict. Try again"
        
    n = len(G)
    for i in G:
        temp[i] = counter
        newG[counter] = i
        counter += 1

    # Create the graph for the KruskalMST function to use
    for i in G:
        for j in G[i]:
            u, v, w = temp[i], temp[j[0]], j[1]
            graph.append([u, v, w])
    # Return the results of the KruskalMST function
    return KruskalMST(graph, counter, newG)


def main():
    print question3({'A': [('B', 2)],
                     'B': [('A', 2),
                           ('C', 5)],
                     'C': [('B', 5)]})
    print question3({})
    print question3(12323)

if __name__ == '__main__':
    main()
