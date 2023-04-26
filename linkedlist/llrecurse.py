class Node:

    def __init__(self,data):
        self.data=data
        self.next = None


def deleteNode(head, val):
    if(head==None):
        print("No element in the list...")
        return 

    if (head.data==val):
        if head.next:
            head.data = head.next.data
            head.next = head.next.next
            return 1
        else: return 0

    if deleteNode(head.next, val)==0:
        head.next = None
        return 1

def push(head, data):
    node = Node(data)
    node.next = head
    head = node
    return node

def printLL(head):
    if head == None:
        return 
    else:
        temp = head 
        while(temp):
            print(temp.data, end=" ")
            temp = temp.next
        print()

head = None
# Adds new element at the
# beginning of the list
head = push(head, 10)
head = push(head, 12)
head = push(head, 14)
head = push(head, 15)
# original list
printLL(head)
# Call to delete function
deleteNode(head, 20)
# 20 is not present thus no change
# in the list
printLL(head)
deleteNode(head, 10)
printLL(head)
deleteNode(head, 14)
printLL(head) 


