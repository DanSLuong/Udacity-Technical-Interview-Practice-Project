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

    # Runs forloop until desired value m
    for i in range(m):
        # Checks to see if ll is empty
        if (p1 == None):
            return None
        # If not empty assign p1.next as the new p1 value
        p1 = p1.next
    while (p1 != None):
        p1 = p1.next
        p2 = p2.next
    # return the value at p2
    return p2.data


def main():
    # Create the BST
    head = Node(10)
    head.next = Node(13)
    head.next.next = Node(2)
    head.next.next.next = Node(73)
    head.next.next.next.next = Node(69)

    print "Test case 1: "
    print question5(head, 3)
    print "Test case 2: " 
    print question5(head, 5)
    print "Test case 3: "
    print question5(head, 1)


if __name__ == '__main__':
    main()
