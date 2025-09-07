class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  # Will be updated to point to the next node
        self.prev = None  # Will be updated to point to the previous node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        if not isinstance(next_node, Node) and next_node is not None:
            raise ValueError("next_node must be a Node instance or None")
        self.next = next_node

    def get_prev(self):
        return self.prev

    def set_prev(self, prev_node):
        if not isinstance(prev_node, Node) and prev_node is not None:
            raise ValueError("prev_node must be a Node instance or None")
        self.prev = prev_node


class CircularDoublyLinkedList:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def add_node(self, data):
        if self.size == self.capacity:
            raise Exception("List is at full capacity")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
        self.size += 1

    def add_node_left(self, data):
        if self.size == self.capacity:
            raise Exception("List is at full capacity")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.head.prev
            new_node.next = self.head
            self.head.prev.next = new_node  # Link the old predecessor to the new node
            self.head.prev = new_node  # Link the current head back to the new node
        self.head = new_node  # Make the new node the current node
        if self.head == 1:
            self.tail = new_node.next
        self.size += 1
        
    def add_node_right(self, data):
        if self.size == self.capacity:
            raise Exception("List is at full capacity")
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.next = new_node.prev = new_node
        else:
            new_node.prev = self.head
            new_node.next = self.head.next
            self.head.next.prev = new_node  # Link the old successor's previous to new node
            self.head.next = new_node  # Link the current head's next to the new node
            if self.head == self.tail:  # If there was only one node before adding
                self.tail = new_node
        self.head = new_node    # Make the new node the current node
        self.size += 1


    def pop(self):
        if self.size == 0:
            raise Exception("List is empty")
        elif self.size == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        self.size -= 1

    def get_current_node(self):
        if not self.head:
            raise Exception("List is empty")
        return self.head
    
    def get_size(self):
        return self.size

    def move_next(self):
        if not self.head:
            raise Exception("List is empty")
        self.head = self.head.next
        self.tail = self.tail.next

    def move_prev(self):
        if not self.head:
            raise Exception("List is empty")
        self.head = self.head.prev
        self.tail = self.tail.prev
        
    def __repr__(self):
        # create the string representation of the linked list
        str_exp = ""
        current = self.head
        while current != None:
            if current.get_next() != None:
                str_exp += str(current.get_data()) + " -> "
            else:
                str_exp += str(current.get_data())
            current = current.get_next()
        return str_exp 
    
    def __str__(self):
        string = ""
          
        if(self.head == None):
            string += "Doubly Circular Linked List Empty"
            return string
          
        string += f"Doubly Circular Linked List:\n{self.head.data}"      
        temp = self.head.next
        while(temp != self.head):
            string += f" -> {temp.data}"
            temp = temp.next
        return string    
        
def test():
    linkedList = CircularDoublyLinkedList(5)
    '''linkedList.append("hi")
    print(linkedList)
    linkedList.append(1)
    print(linkedList)
    linkedList.insert(0, 5)
    print(linkedList)
    linkedList.insert(0, "sup")
    print(linkedList)    
    linkedList.append('bye')
    print(linkedList)
    linkedList.pop()
    print(linkedList)'''
    linkedList.add_node("wee")
    print(linkedList)
    linkedList.add_node("hey")
    print(linkedList)    
test()