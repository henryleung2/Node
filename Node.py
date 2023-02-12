class LinkedListNode(object):
    def __init__(self, value):
        self.value = value
        self.next = None


a = LinkedListNode(0)
b = LinkedListNode(1)
a.next = b


def reverse(a, b):
    swap = a
    a = b
    b = swap

    a.next = b
    return a, b


a, b = reverse(a, b)
a, b = reverse(a, b)
print(a.value)
print(a.next.value)
