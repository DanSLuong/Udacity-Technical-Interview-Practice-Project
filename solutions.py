# Answer the following questions:

##################################################################################
##################################################################################
# Question 1
# Given two strings s and t, determine whether some anagram of t is a substring
# of s. For example: if s = "udacity" and t = "ad", then the function returns
# True. Your function definition should look like: question1(s, t) and return a
# boolean True or False.

def question1(s, t):
    # Get the lengths of strings s and t
    lenT = len(t)
    lenS = len(s)
    # Store values of t inside of a list
    sortT = list(t)
    sortT.sort()

    for i in range(lenS - lenT + 1):
        # Store values of s1 inside of a list
        s1 = list(s[i: i+lenT])
        s1.sort()
        # Compares s1 to s2 and returns the result
        if s1 == sortT:
            return True
    return False


def main():
    print question1("udacity", "ad")
    # Should print True
    print question1("udacity", " ")
    # Should print False
    print question1("udacity", "so")
    # Should print False

if __name__ == '__main__':
    main()


##################################################################################
##################################################################################
# Question 2
# Given a string a, find the longest palindromic substring contained in a.
# Your function definition should look like question2(a), and return a string.

def question2(s):
    # Check for string
    if not s:
        return "No value"
    if type(s) != str:
        return "Not a string"
    # get the length of the string
    n = len(s)
    longest = 0
    
    for i in range(n):
        for j in range(i + 1, n + 1):
            subString = s[i:j]
            # Checks if the subString value is the same when reverse and if longest
            if subString == subString[::-1] and len(subString) > longest:
                # Checks the length of the substring to see if its the longest
                longest = len(subString)
                # Store the i, j values to get the subString
                left = i
                right = j
    # Compute the subString using the stored longest left and right values
    LongSubStr = s[left:right]
    # Return the Longest SubString
    return LongSubStr


def main():
    # Test cases
    TC1 = "racecar"
    print "Test case 1: " + '"' + TC1 + '"' + " longest palindromic subString: " + question2(TC1)
    # Should print      Test case 1: "racecar" longest palindromic subString: racecar
    TC2 = ""
    print "Test case 2: " + '"' + TC2 + '"' + " longest palindromic subString: " + question2(TC2)
    # Should print      Test case 2: "" longest palindromic subString: No value
    TC3 = "udacity"
    print "Test case 3: " + '"' + TC3 + '"' + " longest palindromic subString: " + question2(TC3)
    # Should print      Test case 3: "udacity" longest palindromic subString: u
    TC4 = 5651651
    print "Test case 4: "
    print question2(TC4)
    # Should print      Test case 4: 
    #                   Not a string


if __name__ == '__main__':
    main()


##################################################################################
##################################################################################
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

    # Checks length of G    
    n = len(G)
    
    if n < 2:
        return "There is no connection between two nodes"
    else: 
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
    # Should print {'A': [('B', 2)], 'C': [('B', 5)]}
    print question3({'A': [('B', 2)]})
    # Should print There is no connection between two nodes
    print question3({})
    # Should print List is empty. Try again
    print question3(12323)
    # Should print Not a dict. Try again


if __name__ == '__main__':
    main()





##################################################################################
##################################################################################
# Question 4
# Find the least common ancestor between two nodes on a binary search tree. The
# least common ancestor is the farthest node from the root that is an ancestor
# of both nodes. For example, the root is a common ancestor of all nodes on the
# tree, but if both nodes are descendents of the root's left child, then that
# left child might be the lowest common ancestor. You can assume that both nodes
# are in the tree, and the tree itself adheres to all BST properties. The
# function definition should look like question4(T, r, n1, n2), where T is the
# tree represented as a matrix, where the index of the list is equal to the
# integer stored in that node and a 1 represents a child node, r is a
# non-negative integer representing the root, and n1 and n2 are non-negative
# integers representing the two nodes in no particular order. For example, one
# test case might be
#   question4([[0, 1, 0, 0, 0],
#               [0, 0, 0, 0, 0],
#               [0, 0, 0, 0, 0],
#               [1, 0, 0, 0, 1],
#               [0, 0, 0, 0, 0]],
#               3,
#               1,
#               4)
#   and the answer would be 3.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


class BinarySearchTree(object):
    def __init__(self, root):
        self.root = Node(root)

    # Referenced https://www.geeksforgeeks.org to brush up on BST insert and search
    # Insertion Operation
    def insert(self, val):
        self.insertHelper(self.root, val)
        
    def insertHelper(self, currentNode, val):
        if self.root is None:
            currentNode = currentNode
        else:
            if currentNode.data < val:
                if currentNode.right is not None:
                    self.insertHelper(currentNode.right, val)
                else:
                    currentNode.right = Node(val)
            else:
                if currentNode.left:
                    self.insertHelper(currentNode.left, val)
                else:
                    currentNode.left = Node(val)

    # Search Operation
    def search(self, val):
        return self.searchHelper(self.root, val)

    def searchHelper(self, currentNode, val):
        # Base Case
        if self.root is None:
            return self.root
        else:
            if currentNode:
                if currentNode.data == val:
                    return True
                elif currentNode.data < val:
                    return self.searchHelper(currentNode.right, val)
                else:
                    return self.searchHelper(currentNode.left, val)
        return False


# Least Common Ancestor function
def lca(r, n1, n2):
    # Base Case
    if r is None:
        return None
    # lca is on left if r is bigger than both n1 and n2
    if(r.data > n1 and r.data > n2):
        return lca(r.left, n1, n2)
    # lca is on right if r is smaller than both n1 and n2
    if(r.data < n1 and r.data < n2):
        return lca(r.right, n1, n2)
    return r.data


def question4(T, r, n1, n2):
    # Base case: not a list
    if type(T)!=list:
        return "Not a tree"
    # Base case: empty tree
    if T == [[]]:
        return "Tree is empty"
    BST = BinarySearchTree(r)
    for i in T[r]:
        BST.insert(i)

    # For loop starting at the last value first
    for row in reversed(range(len(T))):
        for i in T[row]:
            BST.insert(i)

    return lca(BST.root, n1, n2)


def main():
    print question4([[0, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0],
                     [1, 0, 0, 0, 1],
                     [0, 0, 0, 0, 0]],
                    3,
                    1,
                    4)
    # Should print 3
    print question4(3,3,1,4)
    # Should print Not a tree
    print question4([[]],3,1,4)
    # Should print Tree is empty


if __name__ == '__main__':
    main()


##################################################################################
##################################################################################
# Question 5
# Find the element in a singly linked list that's m elements from the end. For
# example, if a linked list has 5 elements, the 3rd element from the end is the
# 3rd element. The function definition should look like question5(ll, m), where
# ll is the first node of a linked list and m is the "mth number from the end".
# You should copy/paste the Node class below to use as a representation of a
# node in the linked list. Return the value of the node at that position.


# Node Class Provided
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


def question5(ll, m):
    p1 = ll
    p2 = ll

    # Runs forloop until desired value m to create a empty value
    for i in range(m):
        # Checks to see if ll is empty
        if (p1 == None):
            return None
        # If not empty assign p1.next as the new p1 value
        p1 = p1.next
    # Runs whileloop until it reaches the empty p1 value
    while (p1 != None):
        p1 = p1.next
        p2 = p2.next
    # return the value at p2
    return p2.data


def main():
    # Create the LL
    head = Node(10)
    head.next = Node(13)
    head.next.next = Node(2)
    head.next.next.next = Node(73)
    head.next.next.next.next = Node(69)

    print "Test case 1: "
    print question5(head, 3)
    # Should print 2
    print "Test case 2: " 
    print question5(head, 5)
    # Should print 10
    print "Test case 3: "
    print question5(head, 1)
    # Should print 69


if __name__ == '__main__':
    main()







