class Node:

    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node_at_head(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

    def insert_node_at_end(self, new_node):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    def insert_node_at_middle(self, target_node, new_node):
        if target_node.next is None:
            print("Buddy try inserting at the end")
        else:
            new_node.next = target_node.next
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
        self.head = self.head.next

    def delete_given_node(self, target_data):
        if self.head == target_data:
            self.delete_head()

        previous_node = None
        current_node = self.head

        while current_node and current_node.data != target_data:
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            return "Data not in the linked list"
        else:
            previous_node.next = current_node.next




ll = LinkedList()
ten = Node(10)
fifty = Node(50)
five = Node(5)
one = Node(1)
twenty = Node(20)

ll.insert_node_at_head(ten)
ll.insert_node_at_end(fifty)
ll.insert_node_at_head(five)
ll.insert_node_at_head(one)
ll.insert_node_at_middle(ten, twenty)
ll.print_linked_list()

target_node = ll.search_by_data(10)
print(target_node.next.data)

print("-------------------")
ll.delete_given_node(10)
print(ll.search_by_data(20))
ll.print_linked_list()
# print(ten.next)
