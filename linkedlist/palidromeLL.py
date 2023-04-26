#Function to check if a singly linked list is palindrome

class Node:
    def __init__(self, data):
        self.data= data
        self.next = None

def push(head,data):
    node=Node(data)
    node.next = head
    head = node
    return node

def palindrome(head):
    temp = head

    stack = []

    while(temp is not None):
        stack.append(temp.data)
        temp = temp.next

    temp = head
    pali = True

    while(temp is not None):
        st = stack.pop()
        if temp.data == st:
            pali=True
        else:
            pali=False
            break

        temp = temp.next

    return pali


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)

one.next=two
two.next = three
three.next = four
four.next = five
five.next = six
six.next = seven
seven.next = None

result= palindrome(one)

print("LL Palidrome", result)
