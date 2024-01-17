# https://www.acmicpc.net/problem/1406
# 메모리 : 97676 KB, 시간 : 1140 ms
# 참고 코드 : https://www.acmicpc.net/source/71293355

import sys
input = sys.stdin.readline


class DList:
    class Node:
        def __init__(self, item, prev=None, next=None):
            self.item = item
            self.prev = prev
            self.next = next

    def __init__(self):
        self.head = self.Node(None)
        self.tail = self.Node(None, self.head)
        self.head.next = self.tail
        self.cur = self.tail

    def insert(self, p, item):
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n

    def delete(self, x):
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f

    def print_list(self):
        p = self.head.next
        while p != self.tail:
            if p.next != self.tail:
                print(p.item, end="")
            else:
                print(p.item)
            p = p.next


w = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())

linked_list = DList()
for s in w:
    linked_list.insert(linked_list.tail, s)


for _ in range(n):
    c = sys.stdin.readline().strip().split()
    if (c[0] == 'P'):
        linked_list.insert(linked_list.cur, c[1])
    elif (c[0] == 'L'):
        if (linked_list.cur.prev.prev != None):
            linked_list.cur = linked_list.cur.prev
    elif (c[0] == 'D'):
        if (linked_list.cur.next != None):
            linked_list.cur = linked_list.cur.next
    elif (c[0] == 'B'):
        if (linked_list.cur.prev.prev != None):
            linked_list.delete(linked_list.cur.prev)


linked_list.print_list()
