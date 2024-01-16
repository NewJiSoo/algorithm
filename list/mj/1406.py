import sys


class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next


class Editor():
    def __init__(self):
        self.head = Node('head', None, None)
        self.tail = Node('tail', self.head, None)
        self.head.next = self.tail
        self.cur = self.tail

    def init_insert(self, p, data):
        t = p.prev
        new_node = Node(data, t, p)
        p.prev = new_node
        t.next = new_node

    def cursorB(self):
        if self.cur.prev != self.head:
            if self.cur == self.tail:
                f = self.cur.prev
                f.prev.next = f.next
                self.tail.prev = f.prev
            else:
                f = self.cur.prev.prev
                r = self.cur
                f.next = r
                r.prev = f

    def add_left(self, data):
        if self.cur == self.tail:
            f = self.cur.prev
            new_node = Node(data, f, self.tail)
            f.next = new_node
            self.tail.prev = new_node
            self.cur = self.tail
        else:
            f = self.cur.prev
            r = self.cur
            new_node = Node(data, f, r)
            f.next = new_node
            r.prev = new_node

    def print(self):
        curr_node = self.head.next
        while curr_node != self.tail:
            print(curr_node.data, end="")
            curr_node = curr_node.next
        print()


list_input = sys.stdin.readline().strip()
ll = Editor()

for char in list_input:
    ll.init_insert(ll.tail, char)

num_operations = int(sys.stdin.readline())

for _ in range(num_operations):
    operation = sys.stdin.readline().strip()
    if operation[0] == 'P':
        ll.add_left(operation[2])
    elif operation[0] == 'L':
        if ll.cur.prev != ll.head:
            ll.cur = ll.cur.prev
    elif operation[0] == 'D':
        if ll.cur != ll.tail:
            ll.cur = ll.cur.next
    elif operation[0] == 'B':
        ll.cursorB()

ll.print()
