#Search an element in a Linked List Recursive


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def search(self, li, key):
        if(not li):
            return False

        if li.data == key:
            return True

        return self.search(li.next, key)

if __name__ == "__main__":
    li = LinkedList()

    li.push(1)
    li.push(2)
    li.push(3)
    li.push(4)
 
    key = 4
 
    # Function call
    if li.search(li.head, key):
        print("Yes")
    else:
        print("No")
 
