class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        #empty linkedlist
        self.head = None
        self.n = 0

    def __len__(self):
        return self.n
    #len() can calculate the length of built-in object like string, tuple, but here we have created this linkedlist so we need to write this magic method 

    def insert_at_start(self,data):
        new_node = Node(data) #new node created
        new_node.next = self.head #connecting new node to head
        self.head = new_node #reassign head
        self.n = self.n + 1 #inreament number of nodes

    def append(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.n += 1
            return
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        new_node.next = None
        self.n += 1
    
    def traversal(self):
        current = self.head
        while current is not None:
            print(str(current.data) + " -> ", end="")
            current = current.next
        else:
            print("None")

    def pop(self):
        if self.head is None:
            raise IndexError("Linked List is empty !!")
        elif self.head.next is None:
            self.head = None
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.n -= 1

    def insert_after(self, after, data):
        new_node = Node(data) #value is that number after which we want to insert the data
        if self.head == None:
            self.append(data)
        else:
            current = self.head
            while current.data != after:
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.n += 1

    def clear(self):
        self.head = None
        self.n = 0
        return "Empty LinkedList"

    def delete_from_start(self):
        if self.head is None:
            return "Empty LinkedList"
        else:
            self.head = self.head.next
            self.n -= 1

    def pop(self):
        if self.head is None:
            return "Empty LinkedList"
        
        elif self.head.next is None:
            self.head = None
            self.n -= 1
            
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            current.next = None
            self.n -= 1

    def delete_by_value(self, value):
        if self.head is None:
            return "Empty LinkedList"
        
        elif self.head.data == value:
            self.head = self.head.next
            self.n -= 1

        else:
            current = self.head
            while current.next is not None and current.next.data != value:
                current = current.next
            
            if current.next is None:
                return "Item not found"
            
            current.next = current.next.next
            self.n -= 1

    def search_by_value(self, value):
        current = self.head
        index = -1
        while current is not None:
            index += 1
            if current.data == value:
                return f"{current.data} at index {index}"
            current = current.next
        return "Element not found"

    def search_by_index(self, index):
        if self.head is None:
            return "Empty LinkedList"

        elif (self.n <= index and index >= 0):
            return "Invalid Index"

        else:
            i = 0
            current = self.head
            while i != index:
                i += 1
                current = current.next
            return f"Data at index {index} is {current.data}"

    def max(self):
        if self.head is None:
            return "Empty Linked List"
        current = self.head.next
        maximum = self.head.data
        while current is not None:
            if current.data > maximum:
                maximum = current.data
            current = current.next

        return maximum

    def replace_with_max(self, value):
        maximum = self.max()

        if self.head is None:
            return "Empty Linked List"
        
        current = self.head
        while current is not None:
            if current.data == maximum:
                current.data = value
                break
            current = current.next
        return "Maximum Value replaced successfully"

    def sum_odd_indices(self):
        total = 0
        current = self.head
        index = 0

        if current is None:
            return "Empty Linked List"
        while current is not None:
            if index % 2 != 0:
                total = total + current.data

            current = current.next
            index = index + 1
        return total

    def reverse(self):
        if self.head is None:
            return "Empty Linked List"
        
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        self.head = previous

if __name__=="__main__":
    L = LinkedList()
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    print("After Appending: ", end="")
    L.traversal()
    L.insert_after(3, 45)
    print("After Inserting in between: ", end="")
    L.traversal()
    L.delete_from_start()
    print("After Deleting from top: ", end="")
    L.traversal()
    L.pop()
    print("After poping: ", end="")
    L.traversal()
    L.delete_by_value(45)
    print("After deleting by value: ", end="")
    L.traversal()
    print(L.search_by_value(4))
    print(L.search_by_index(2))
    L.traversal()
    print(L.max())
    L.replace_with_max(26)
    L.traversal()
    L.append(5)
    L.traversal()
    print(L.sum_odd_indices())
    L.reverse()
    L.traversal()

    # L.insert_at_start(26)
    # L.insert_at_start(7)
    # L.insert_at_start(18)
    # L.insert_at_start(33)
    # L.insert_at_start(10)
    # L.traversal()
    # L.append(45)
    # # print("No.of Element in LinkedList ",len(L))
    # L.traversal()
    # L.pop()
    # L.traversal()
    # L.insert_in_between(18, 45)
    # L.traversal()

    # a = Node(1)
    # b = Node(2)
    # c = Node(3)

    # a.next = b
    # b.next = c

    # print(a.next.data) #a.next reference to the node object b, not to the data stored in node b
    # print(b.next.data)
    # print(c.next)