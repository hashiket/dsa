class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, data):
        node = Node(data)
        node.next = self.head

        if self.head != None:
            self.head.prev = node
        self.head = node 

    def printLL(self):
        temp = self.head

        while temp != None:
            print(temp.data)

            temp = temp.next

    def sortK(self, key):
        if self.head == None or self.head.next == None:
            return 

        i = self.head.next

        while i!= None:
            j = i 
            while j.prev != None and (j.data < j.prev.data):

                temp = j.prev.prev
                temp2 = j.prev
                temp3 = j.next
                j.prev.next = temp3
                j.prev.prev = j
                j.prev = temp
                j.next = temp2
                if temp != None:
                    temp.next = j
                if temp3 != None:
                    temp3.prev = temp2

            if j.prev == None:
                self.head = j
            i = i.next



ll = LinkedList()
ll.push(10)
ll.push(30)
ll.push(20)
ll.push(60)

ll.push(50)
ll.push(40)


ll.printLL()
                
ll.sortK(2)

print("##############")

ll.printLL()

# # Python implementation to sort a k sorted doubly linked list
# import heapq
# head = None

# # a node of the doubly linked list
# class Node:
# 	def __init__(self, data):
# 		self.data = data
# 		self.next = None
# 		self.prev = None

# # function to sort a k sorted doubly linked list
# def sortAKSortedDLL(head, k):
# 	# if list is empty
# 	if head == None:
# 		return head

# 	pq = []

# 	newHead = None
# 	last = None

# 	for i in range(k+1):
# 		# push the node
# 		heapq.heappush(pq, (head.data, head))
# 		# move to the next node
# 		head = head.next

# 	# loop till there are elements in 'pq'
# 	while len(pq) > 0:

# 		if newHead == None:
# 			newHead = heapq.heappop(pq)[1]
# 			newHead.prev = None

# 		# 'last' points to the last node of the result sorted list so far
# 			last = newHead
# 		else:
# 			last.next = heapq.heappop(pq)[1]
# 			last.next.prev = last
# 			last = last.next

# 		# if there are more nodes left in the input list
# 		if head != None:
# 			# push the node
# 			heapq.heappush(pq, (head.data, head))

# 			# move to the next node
# 			head = head.next

# 	# making 'next' of last node point to NULL
# 	last.next = None

# 	# new head of the required sorted DLL
# 	return newHead

# # Function to insert a node at the beginning of the Doubly Linked List
# def push(new_data):

# 	global head

# 	# allocate node
# 	new_node = Node(new_data)

# 	# since we are adding at the beginning, prev is always NULL
# 	new_node.prev = None

# 	# link the old list of the new node
# 	new_node.next = head

# 	# change prev of head node to new node
# 	if (head != None):
# 		head.prev = new_node

# 	# move the head to point to the new node
# 	head = new_node


# # Function to print nodes in a given doubly linked list
# def printList(head):
# 	# if list is empty
# 	if head is None:
# 		print("Doubly Linked list empty")

# 	while head is not None:
# 		print(head.data, end=" ")
# 		head = head.next


# # Driver code
# if __name__ == '__main__':

# 	# Create the doubly linked list:
# 	# 3<->6<->2<->12<->56<->8
# 	push(8)
# 	push(56)
# 	push(12)
# 	push(2)
# 	push(6)
# 	push(3)

# 	k = 2

# 	print("Original Doubly linked list:")
# 	printList(head)

# 	sortedDLL = sortAKSortedDLL(head, k)

# 	print("\nDoubly Linked List after sorting:")
# 	printList(sortedDLL)

