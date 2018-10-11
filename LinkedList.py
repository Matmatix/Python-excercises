class Node(object):
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList(Node):

    def __init__(self, head=None):
        self.head = head

    def add_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = Node(data)

    def iterate(self):
        cur = self.head
        node_array = []
        while cur is not None:
            node_array.append(cur)
            cur = cur.next
        return node_array

    def print_ll(self):
        for item in self.iterate():
            try:
                print("Data: ", item.data, " | Next: ", item.next.data)
            except AttributeError:
                print("Data: ", item.data, " | Next: None")

    def remove_node(self, node_data):
        cur = self.head
        if cur.data == node_data:
            self.head = cur.next
        else:
            while cur.next.data is not node_data:
                cur = cur.next
            cur.next = cur.next.next

    def reverse(self):
        reverse_list = []
        normal_list = []
        for item in self.iterate():
            normal_list.append(item)

        index = 0
        while index < len(normal_list):
            reverse_list.append(normal_list[-1 * (index + 1)])
            index += 1
        return reverse_list