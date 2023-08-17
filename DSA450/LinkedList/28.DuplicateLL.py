#Clone a linked list with next and random pointer


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.arbit = None


def cloneLinkedList(head):
    mp = {}
    temp = head
    nhead = Node(temp.data)
    mp[temp] = nhead

    while temp.next:
        nhead.next = Node(temp.next.data)
        temp = temp.next
        nhead = nhead.next
        mp[temp] = nhead

    temp = head
    while temp:
        mp[temp].arbit = mp[temp.arbit]
        temp=temp.next

    return mp[head]

def printList(head):
    result = []
    while head:
        result.append(f"{head.data}({head.arbit.data})")
        head = head.next
    print(" -> ".join(result))
 
# Creating a linked list with random pointer
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.arbit = head.next.next
head.next.arbit = head
head.next.next.arbit = head.next.next.next.next
head.next.next.next.arbit = head.next.next
head.next.next.next.next.arbit = head.next
 
# Print the original list
print("The original linked list:")
printList(head)
 
# Function call
sol = cloneLinkedList(head)
 
print("The cloned linked list:")
printList(sol)