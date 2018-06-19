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


if __name__ == '__main__':
    main()
