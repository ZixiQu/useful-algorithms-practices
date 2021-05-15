class Stack():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def pop(self):
        if self.is_empty():
            raise ValueError("pop from empty stack")
        return self.items.pop()

    def push(self, item):
        self.items.append(item)


class Queue():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("pop from empty stack")
        return self.items.pop(0)

class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return "{} -> {}".format(self.value, self.next)

class LList():
    def __init__(self):
        self.head , self.tail = None, None

    def __len__(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next
        return count

    def __contains__(self, value):
        curr = self.head
        while curr:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def __str__(self):
        if not self.head:
            return "empty"
        return self.head.__str__()
    def append(self, item):
        """ item append to the head of linkedlist"""
        if not self.head:
            assert not self.tail
            self.head, self.tail = item, item
            return
        item.next = self.head
        self.head = item
        return

    def delete(self, value):
        """ delete the first occurence of <value>. Return True on successful deletion."""
        if self.head is None:
            return False
        if self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        curr = self.head
        prev = None
        while curr.next is not None:
            if curr.next.value == value:
                curr.next = curr.next.next
                if curr.next is None:
                    self.tail = curr
                return True
            prev = curr
            curr = curr.next
        if curr == value:
            prev.next = None
            self.tail = prev
            return True
        return False


if __name__ == "__main__":
    l = LList()
    l.append(Node(3))
    l.append(Node(5))
    l.append(Node(7))

    s = Queue()
    s.enqueue(3)
    s.enqueue(5)
    print(s.dequeue())
    print(s.is_empty())






