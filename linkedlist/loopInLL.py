#Detect loop in a linked list

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

    def printList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data, end=" ")
            temp = temp.next

    def loop(self):
        st = set()
        temp = self.head

        while(temp):
            if temp in st:
                return True
            st.add(temp)
            temp = temp.next
            
        return False


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)

#ll.head.next.next.next.next = ll.head

if(ll.loop()):
    print("Loop Found")
else:
    print("Loop not Found")