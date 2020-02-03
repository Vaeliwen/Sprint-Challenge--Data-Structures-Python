from doubly_linked_list import DoublyLinkedList
from doubly_linked_list import ListNode


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        self.length = 0



    def append(self, item):
        if self.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
            self.length += 1
        elif self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            new_node = ListNode(item, self.current, self.current.next)
            self.current.next.prev = new_node
            self.current.next = new_node
            self.storage.delete(new_node.next)
            self.current = new_node
            self.storage.length += 1
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        read_pointer = self.storage.head
        while len(list_buffer_contents) < self.length:
            list_buffer_contents.append(read_pointer.value)
            read_pointer = read_pointer.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

buffer = RingBuffer(5)

#buffer.append("a")
#buffer.append("b")
#buffer.append("c")
#buffer.append("d")
#buffer.append("e")
#buffer.append("f")
#print(buffer.get())
