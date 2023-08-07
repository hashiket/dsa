#Find the start of loop

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printll(head):
    temp = head 

    while temp:
        print(temp.data)
        temp = temp.next

    
def stofLoop(head):
    if head==None or head.next == None:
        return None

    slow = head
    fast = head
    slow = slow.next
    fast = fast.next.next
    while fast and fast.next:

        if fast == slow:
            break

        slow = slow.next
        fast = fast.next.next 

    if slow!=fast:
        return None

    slow = head
    while slow!=fast:
        slow= slow.next
        fast = fast.next

    return slow


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

head.next.next.next.next.next = head.next.next
st = stofLoop(head)
print(st.data)

#printll(head)



        