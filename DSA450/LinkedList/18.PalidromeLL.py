#Write a Program to check whether the Singly Linked list is a palindrome or not.

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

    def palidrome(self):
        temp = self.head
        stack = []
        while temp!=None:
            stack.append(temp.data)
            temp = temp.next
        temp = self.head
        print(stack)
        while temp!=None:
            s = stack.pop()
            print(s)
            if s!=temp.data:
                return False
            temp = temp.next
        return True
            

ll = LinkedList()
ll.push(10)
ll.push(20)
ll.push(10)


ll.printLL()

print(ll.palidrome())
