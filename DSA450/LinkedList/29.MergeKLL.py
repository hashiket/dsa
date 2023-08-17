#Merge K sorted linked lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None 

def printLL(head):
    temp = head

    while temp!=None:
        print(temp.data)
        temp = temp.next 

def mergeKLists(arr, last):
    for i in range(1, last+1):
        while True:

            head_0 = arr[0]
            head_i = arr[i]

            if head_i == None:
                break

            if head_0.data>=head_i.data:
                arr[i] = head_i.next
                head_i.next = head_0
                arr[0] = head_i
            else:
                while head_0.next!=None:
                    if head_0.next.data>=head_i.data:
                        arr[i] = head_i.next
                        head_i.next = head_0.next
                        head_0.next = head_i
                        break
                    head_0 = head_0.next

                    if head_0.next == None:
                        arr[i] = head_i.next
                        head_i.next = None
                        head_0.next = head_i
                        head_0.next.next = None
                        break
    return arr[0]


if __name__ == '__main__':
  
    # Number of linked
    # lists
    k = 3
  
    # Number of elements
    # in each list
    n = 4
  
    # an array of pointers
    # storing the head nodes
    # of the linked lists
    arr = [None for i in range(k)]
  
    arr[0] = Node(1)
    arr[0].next = Node(3)
    arr[0].next.next = Node(5)
    arr[0].next.next.next = Node(7)
  
    arr[1] = Node(2)
    arr[1].next = Node(4)
    arr[1].next.next = Node(6)
    arr[1].next.next.next = Node(8)
  
    arr[2] = Node(0)
    arr[2].next = Node(9)
    arr[2].next.next = Node(10)
    arr[2].next.next.next = Node(11)
  
    # Merge all lists
    head = mergeKLists(arr, k - 1)
  
    printLL(head)















#     def SortedMerge(a, b):
  
#     result = None
  
#     # Base cases
#     if (a == None):
#         return(b)
#     elif (b == None):
#         return(a)
  
#     # Pick either a or b, and recur
#     if (a.data <= b.data):
#         result = a
#         result.next = SortedMerge(a.next, b)
#     else:
#         result = b
#         result.next = SortedMerge(a, b.next)
  
#     return result
  
# # The main function that takes an array of lists
# # arr[0..last] and generates the sorted output
# def mergeKLists(arr, last):
  
#     # Repeat until only one list is left
#     while (last != 0):
#         i = 0
#         j = last
  
#         # (i, j) forms a pair
#         while (i < j):
  
#             # Merge List i with List j and store
#             # merged list in List i
#             arr[i] = SortedMerge(arr[i], arr[j])
  
#             # Consider next pair
#             i += 1
#             j -= 1
  
#             # If all pairs are merged, update last
#             if (i >= j):
#                 last = j
  
#     return arr[0]
  