#Multiply two linked lists


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

        while temp:
            print(temp.data)
            temp = temp.next

def multiplyTwoLists(first, second):
    l1 = first.head
    l2 = second.head
    num = 0
    num2 = 0
    while l1!=None or l2!=None:
        if l1!=None:
            num = num*10 + l1.data
            l1 = l1.next
        
        if l2!=None:
            num2 = num2*10 + l2.data
            l2 = l2.next

    return num*num2


if __name__=='__main__':
    
    first = LinkedList()
    second = LinkedList()
    
    # Create first Linked List 9->4->6
    first.push(6)
    first.push(4)
    first.push(9)
  
    # Printing first Linked List
    print("First list is: ", end = '')
    first.printLL()
    
    # Create second Linked List 8->4
    second.push(4)
    second.push(8)
  
    # Printing second Linked List
    print("Second List is: ", end = '')
    second.printLL()
    
    # Multiply two linked list and
    # print the result
    result = multiplyTwoLists(first, second)
    print("Result is: ", result)
  
