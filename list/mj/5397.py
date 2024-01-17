# https://www.acmicpc.net/problem/5397
# 메모리 : 119112 KB, 시간 : 4824 ms
# 참고 코드 : https://www.acmicpc.net/source/69055389

import sys


class Node(object):
    def __init__(self, item=0, prev=None, next=None):
        self.item = item
        self.prev = prev
        self.next = next


N = int(sys.stdin.readline())


for _ in range(N):
    M = list(input())  # sys를 사용하면 안됨. (개행까지 포함해서 읽어버림 )
    password = Node()
    print_password = password

    for i in M:
        if i == '<':
            if password.prev:
                password = password.prev

        elif i == '>':
            if password.next:
                password = password.next

        elif i == '-':
            if password.prev:
                prev_node = password.prev
                next_node = password.next

                prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
                password = prev_node
        else:
            new_node = Node(i)
            next_node = password.next

            if next_node:
                next_node.prev = new_node

            new_node.next = next_node

            password.next = new_node
            new_node.prev = password
            password = new_node

    current = print_password.next  # 첫번째 prev는 값이 없으니 제외
    while current:
        print(current.item, end="")  # 개행없이 한줄에 나오도록
        current = current.next
    print()  # 기본적으로는 출력된 값 뒤에 개행 문자('\n')가 추가
    # 첫번째 테스트 케이스의 출력이 끝나면 개행, 두번째로 넘어감
