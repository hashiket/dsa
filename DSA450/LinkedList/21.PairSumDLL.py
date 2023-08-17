#Find pairs with a given sum in a DLL.

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self, data):
        node = Node(data)
        node.next = self.head
        
        if self.head !=None:
            self.head.prev = node

        self.head = node

    def printLL(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp=temp.next

    def pairsum(self, key):
        first = self.head

        last = self.head

        while last.next != None:
            last=last.next

        found = False

        while (first != last and last.next!=first):
            if(first.data+last.data==key):
                found = True

                print(f"First: {first.data} Second:{last.data}")

                first = first.next
                last = last.prev

            else:
                if(first.data+last.data<key):
                    first=first.next
                else:
                    last = last.prev

        if(found==False):
            print("Pair not Found!!!")


ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)

ll.printLL()

ll.pairsum(50)

