#Delete nodes which have a greater value on right side


# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def push(self, data):
#         node = Node(data)
#         node.next = self.head

#         self.head = node

#     def printLL(self):
#         temp = self.head 

#         while temp is not None:
#             print(temp.data)
#             temp = temp.next


#     def delLesserNode(self):
#         self.reverseList()

#         self._delLesserNode()

#         self.reverseList()


#     def _delLesserNode(self):
#         curr = self.head
#         maxNode = self.head

#         while curr is not None and curr.next is not None:
#             if curr.next.data < maxNode.data:
#                 temp = curr.next
#                 curr.next = temp.next

#             else:
#                 curr = curr.next
#                 maxNode = curr

#     def reverseList(self):
#         curr = self.head
#         prev = None
#         while curr is not None:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next

#         self.head = prev


# # 12->15->10->11->5->6->2->3

# ll = LinkedList()

# ll.push(3)
# ll.push(2)
# ll.push(6)
# ll.push(5)
# ll.push(11)
# ll.push(10)
# ll.push(15)
# ll.push(12)
# ll.printLL()
# ll._delLesserNode()
# print("#################")
# ll.printLL()



# Python program to delete nodes which have a
# greater value on right side
class Node:

	# constructor to initialize the node object
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	# Function to initialize head
	def __init__(self):
		self.head = None

	# Function to insert a new node at beginning
	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node

	# Utility function to print a linked list
	def printList(self):
		temp = self.head
		while(temp is not None):
			print(temp.data, end=" ")
			temp = temp.next
		print("\n")

	def delLesserNodes(self):
		# Reverse the linked list
		self.reverseList()

		# In the reversed list, delete nodes which have a node with greater
		# value node on left side. Note that head node is never deleted because
		# it is the leftmost node.
		self._delLesserNodes()

		# Reverse the linked list again to retain the original order
		self.reverseList()

	# Deletes nodes which have greater value node(s) on left side
	def _delLesserNodes(self):
		current = self.head
		# Initialize max
		maxnode = self.head

		while(current is not None and current.next is not None):
			# If current is smaller than max, then delete current
			if(current.next.data < maxnode.data):
				temp = current.next
				current.next = temp.next

			# If current is greater than max, then update max and move current
			else:
				current = current.next
				maxnode = current

	# Utility function to reverse a linked list
	def reverseList(self):
		current = self.head
		prev = None
		while(current is not None):
			next = current.next
			current.next = prev
			prev = current
			current = next
		self.head = prev


# Create following linked list
# 12->15->10->11->5->6->2->3
llist = LinkedList()
llist.push(3)
llist.push(2)
llist.push(6)
llist.push(5)
llist.push(11)
llist.push(10)
llist.push(15)
llist.push(12)

print("Given linked list")
llist.printList()

llist.delLesserNodes()

print("Modified Linked List")
llist.printList()

# This code is contributed by Yash Agarwal(yashagarwal2852002)
