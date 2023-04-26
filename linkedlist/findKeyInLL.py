#Search an element in a Linked List Iterative

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head =  None

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node 

    def search(self, x):
        temp = self.head

        while(temp):
            if temp.data == x:
                return True
            temp=temp.next
        else:
            return False

if __name__ == "__main__":
    llist = LinkedList()
 
    ''' Use push() to construct below list
        14->21->11->30->10 '''
    llist.push(10)
    llist.push(30)
    llist.push(11)
    llist.push(21)
    llist.push(14)
 
       # Function call
    if llist.search(21):
        print("Yes")
    else:
        print("No")