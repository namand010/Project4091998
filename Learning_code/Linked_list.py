class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def create_linked_list_better(input_list):

        head = None
        tail = None

        for value in input_list:

            if head is None:
                head = Node(value)
                tail = head  # when we only have 1 node, head and tail refer to the same node
            else:
                tail.next = Node(value)  # attach the new node to the `next` of tail
                tail = tail.next  # update the tail

        return head

    def print_linked_list(head):
        current_node = head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next


#print_linked_list(head)
head = Node(2)
#new_node = Node(1)
#head.next = new_node
head.next = Node(1)

#print(new_node.value)
print(head.next.value)