class Node:

    def __init__(self, data, next = None, previous = None):
        self.data = data
        self.next = next
        self.prev = previous

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_head(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_doubly_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_node_at_end(self, new_node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
        new_node.prev = current_node

    def insert_node_at_middle(self, target_node, new_node):
        if target_node.next is None:
            print("Buddy try inserting at the end")
        else:
            new_node.next = target_node.next
            new_node.prev = target_node

            target_node.next.prev = new_node
            target_node.next = new_node


    def search_by_data(self, target_data):
        if not target_data:
            return "No data provided"

        current_node = self.head
        while current_node:
            if current_node.data == target_data:
                return current_node
            current_node = current_node.next
        return "Data not found"

    def delete_head(self):
        if self.head is None:
            print("The list is empty.")
        else:
            self.head = self.head.next

    def delete_given_node(self, target_data):
        if self.head == target_data:
            self.delete_head()

        previous_node = None
        current_node = self.head

        while current_node and current_node.data != target_data:
            current_node = current_node.next

        if current_node is None:
            return "Data not in the linked list"

        current_node.prev.next = current_node.next
        if current_node.next is not None:
            current_node.next.prev = current_node.prev


        else:
            previous_node.next = current_node.next

dll = DoublyLinkedList()
ten = Node(10)
fifty = Node(50)
five = Node(5)
one = Node(1)
twenty = Node(20)

dll.insert_node_at_head(ten)
dll.insert_node_at_head(fifty)
dll.insert_node_at_middle(fifty, twenty)
# dll.delete_given_node(20)
dll.insert_node_at_middle(twenty, Node(15))
dll.print_doubly_linked_list()