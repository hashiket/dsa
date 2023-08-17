#Find the middle Element of a linked list.

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


    def printLL(self):
        temp = self.head
        while temp != None:
            print(temp.data)
            temp= temp.next


    # def middleElement(self):
    #     temp = self.head
    #     ct=0
    #     while temp != None:
    #         ct+=1
    #         temp= temp.next
    #     mid=ct//2
    #     ct1=0
    #     temp = self.head
    #     while temp != None:
    #         if ct1==mid:
    #             print(temp.data)
    #             break
    #         ct1+=1
    #         temp= temp.next
    def middleElement(self):
        slow = self.head
        fast = self.head
        while fast!=None and fast.next!=None:
            slow=slow.next
            fast = fast.next.next
        return slow.data
        

ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(30)
ll.push(40)
ll.push(50)
ll.push(60)

ll.printLL()

print(ll.middleElement())
