class Node:

    def __init__(self,data):
        self.data=data
        self.next = None

class Linklist:
    
    def __init__(self):
        self.head = None

    def push(self, new_data):
        node = Node(new_data)
        node.next = self.head
        self.head = node

    def insert_after(self,pre_node, new_data):

        if pre_node is None:
            print(" The given node must in linklist")
            return 

        node = Node(new_data)
        node.next = pre_node.next
        pre_node.next = node

    def append(self, new_data):

        node = Node(new_data)

        if self.head is None:
            self.head = node
            return

        last = self.head

        while(last.next):
            last = last.next

        last.next = node

    def printList(self):
        temp =  self.head
        while(temp):
            print(temp.data, end=" ")
            temp=temp.next 
        

if __name__ == '__main__':
    llist = Linklist()

    llist.append(6)

    llist.push(7)

    llist.push(1)

    llist.append(4)

    llist.insert_after(llist.head.next,8)

    llist.printList()