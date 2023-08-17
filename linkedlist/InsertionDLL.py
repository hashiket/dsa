def push(self, data):
    node = Node(data)
    node.next = self.head
    node.prev =  None
    if self.head != None:
        self.head.prev = node

    self.head = node

def insertAfter(self, prev, data):
    if prev is None:
        return

    node = Node(data)
    node.next = prev.next
    prev.next = node 
    node.prev = prev

    if node.next != None:
        node.next.prev = node

     
def insetBefore(self, prev_node, data):
    if prev_node is None:
        return None

    node = Node(data)
    node.prev = prev_node.prev
    prev_node.prev = node
    node.next = prev_node

    if node.prev != None:
        node.prev.next = node
    else:
        head = node


def append(self, data):
    node = Node(data)
    node.next = None

    if self.head is None:
        node.prev = None
        self.head = node
        return
    
    temp = self.head

    while temp!=None:
        temp = temp.next

    temp.next = node
    node.prev = temp
        
