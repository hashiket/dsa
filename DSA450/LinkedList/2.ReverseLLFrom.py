#Reverse a Linked List in group of Given Size. [Very Imp]

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
            temp= temp.next


    def reverse(self,head, k):
        if head == None:
          return None
        curr=head
        prev=None
        next=None
        cnt = 0
        while curr is not None and cnt<k:
            next=curr.next
            curr.next = prev
            prev = curr
            curr=next
            cnt+=1

        if next is not None:
            head.next = self.reverse(next, k)

        return prev 


ll = LinkedList()
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
ll.push(5)
# ll.push(6)
# ll.push(7)
# ll.push(8)

ll.printll()
print("**************")
ll.head = ll.reverse(ll.head, 3)

ll.printll()







#####################################################################
# Python program to reverse a linked list in groups of given size
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
  
# Reverses the linked list in groups
# of size k and returns the pointer
# to the new head node.
  
  
def reverse(head, k):
  # If head is NULL or K is 1 then return head
    if not head or k == 1:
        return head
    dummy = Node(-1)  # creating dummy node
    dummy.next = head
    # Initializing three points prev, curr, next
    prev = dummy
    curr = dummy
    next = dummy
    count = 0
    toLoop = 0
    i = 0
  
    # Calculating the length of linked list
    while curr:
        curr = curr.next
        count += 1
  
    # Iterating till next is not none
    while next:
        curr = prev.next  # Curr position after every reversed group
        next = curr.next  # Next will always next to curr
        # toLoop will set to count - 1 in case of remaining element
        toLoop = count > k and k or count - 1
        for i in range(1, toLoop):
                # 4 steps as discussed above
            curr.next = next.next
            next.next = prev.next
            prev.next = next
            next = curr.next
        # Setting prev to curr
        prev = curr
        # Update count
        count -= k
  
     # dummy -> next will be our new head for output linked list
    return dummy.next
  
# Function to print linked list
  
  
def printList(node):
    while node is not None:
        print(node.data, end=" ")
        node = node.next
  
  
# Created Linked list is 1->2->3->4->5->6->7->8->9
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)
head.next.next.next.next.next.next = Node(7)
head.next.next.next.next.next.next.next = Node(8)
head.next.next.next.next.next.next.next.next = Node(9)
  
print("Given linked list")
printList(head)
head = reverse(head, 3)
  
print("\nReversed Linked list")
printList(head)
  

        

