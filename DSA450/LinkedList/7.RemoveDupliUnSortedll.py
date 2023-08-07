#Remove Duplicates from unsorted ll

#T-O(N^2) S-O(1)
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self, data):
#         node = Node(data)
#         node.next = self.head
#         self.head = node

#     def printll(self):
#         temp = self.head
#         while temp:
#             print(temp.data)
#             temp = temp.next

#     def removeDuplicate(self):
#         if self.head is None:
#             return None

#         temp = self.head
#         temp1=None

#         while temp!=None and  temp.next != None:
#             temp1=temp 
#             while temp1.next != None:
#                 if temp.data == temp1.next.data:
#                     temp1.next = temp1.next.next
#                 else:
#                     temp1 = temp1.next
#             temp=temp.next


#T-O(N) S-O(N)
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

    def printll(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def removeDuplicate(self):
        if self.head is None:
            return None

        temp = self.head
        s = set()
        s.add(self.head.data)

        while temp.next != None:
            if temp.next.data in s:
                temp.next = temp.next.next
            else:
                s.add(temp.next.data)
                temp=temp.next
        




ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(1)
ll.push(4)
ll.push(5)
ll.push(4)

ll.printll()

ll.removeDuplicate()
print("####*****")

ll.printll()