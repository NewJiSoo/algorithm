class Node:
    def __init__(self, value=0, next=None, prev=None):
        self.value = value
        self.next_ = next
        self.prev = prev


class LinkedList(object):
    def __init__(self):
        self.size = 0  # node의 개수
        self.head = None
        self.tail = None

    # 시간복잡도 - O(1)
    def insert_back(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next_ = new_node
            new_node.prev = self.tail  # doubly에는 이게 추가됨
            self.tail = self.tail.next_
        self.size += 1

    # 시간복잡도 - O(n)
    # 예외사항1 : if self.head is None
    # 예외사항2 : if idx < 0 or idx > self.size
    def insert_at(self, idx, value):
        new_node = Node(value)
        if idx == 0:
            new_node.next_ = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next_
            new_node.next_ = current.next_
            current.next_.prev = new_node

            current.next_ = new_node
            new_node.prev = current
        self.size += 1

    # 시간복잡도 - O(1)
    def remove_back(self):  # => 이걸 구현 하려면 doubly linked list 여야 한다.
        self.tail = self.tail.prev
        self.tail.next_ = None
        self.size -= 1

    # 시간복잡도 - O(n)
    def remove_at(self, idx):
        if idx == 0:
            self.head = self.head.next_
            self.head.prev = None  # garbage collector가 알아서 처리해준다.
        else:
            current = self.head
            for _ in range(idx - 1):
                current = current.next_

            current.next_ = current.next_.next_
            current.next_.prev = current  # garbage collector가 알아서 처리해준다.
        self.size -= 1

    # 시간복잡도 - O(n)
    # 예외상황: if idx < 0 or idx >= self.size
    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next_
        return current.value

    # 시간복잡도 - O(n)
    # 예외상황: if idx < 0 or idx >= self.size
    def set(self, idx, value):
        current = self.head
        for _ in range(idx):
            current = current.next_
        current.value = value

    def print(self):
        current = self.head
        while current:
            print(current.value, end="")
            current = current.next_
            if current:
                print("->", end="")
        print()
