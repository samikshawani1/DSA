class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    # Insert at the end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node
        new_node.prev = temp

    # Display forward
    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    # Display backward
    def display_backward(self):
        if self.head is None:
            return

        temp = self.head

        # Move to last node
        while temp.next:
            temp = temp.next

        # Traverse backwards
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")


# Create DLL
dll = DoublyLinkedList()

n = int(input("Enter number of nodes: "))

for i in range(n):
    value = int(input(f"Enter value {i+1}: "))
    dll.insert(value)

print("\nForward Traversal:")
dll.display_forward()

print("Backward Traversal:")
dll.display_backward()