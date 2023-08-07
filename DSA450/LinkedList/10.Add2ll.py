#Add two number represented by Linked Lists :
#T-O(m+n) S-O(m+n)
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

def addLL(ll1,ll2):
    sum1=0
    sum2=0
    while ll1.head:
        sum1= sum1*10+ll1.head.data
        ll1.head = ll1.head.next

    while ll2.head:
        sum2 = sum2*10 + ll2.head.data
        ll2.head = ll2.head.next

    sum = sum1 +sum2

    new = LinkedList()
    while sum>0:
        last = sum%10
        new.push(last)
        sum=sum//10

    return new


first = LinkedList()
second = LinkedList()
first.push(6)
first.push(4)
first.push(9)
first.push(5)
first.push(7)
 
second.push(4)
second.push(8)
 
ans = addLL(first, second)
 
print("Sum is : ", end=' ')
ans.printll()



        
