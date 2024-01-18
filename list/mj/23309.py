# https://www.acmicpc.net/problem/23309
# 시간초과

import sys

N, M = map(int, sys.stdin.readline().split())
Y_list = list(map(int, sys.stdin.readline().split()))


class Node(object):
    def __init__(self, item=0, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


station = Node()
current = station

for i in Y_list:
    new_node = Node(i)
    current.next = new_node
    new_node.prev = current
    current = new_node

# 연결 리스트를 원형으로 만들기
current.next = station.next
station.next.prev = current

for _ in range(M):
    x = list(map(str, input().split()))

    if x[0] == 'BN':
        while current.item != int(x[1]):
            current = current.next
        print(current.next.item)

        new_node = Node(int(x[2]))

        next_node = current.next

        new_node.next = next_node
        current.next = new_node
        new_node.prev = current
        next_node.prev = new_node

    elif x[0] == 'BP':
        while current.item != int(x[1]):
            current = current.next
        print(current.prev.item)

        new_node = Node(int(x[2]))

        prev_node = current.prev
        new_node.prev = prev_node
        prev_node.next = new_node
        current.prev = new_node
        new_node.next = current

    elif x[0] == 'CN':
        while current.item != int(x[1]):
            current = current.next

        remove_node = current.next
        link_node = remove_node.next

        current.next = link_node
        link_node.prev = current

        print(remove_node.item)

    elif x[0] == 'CP':
        while current.item != int(x[1]):
            current = current.next

        remove_node = current.prev
        link_node = remove_node.prev

        current.prev = link_node
        link_node.next = current

        print(remove_node.item)
