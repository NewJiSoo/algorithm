# https://www.acmicpc.net/problem/14426
# 메모리 : 35212 KB, 시간 : 1476 ms
# trie 자료구조를 이용한 방법

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_world = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root  # root는 빈 노드
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.end_world = True

    def is_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True


N, M = map(int, input().split())

trie = Trie()
for _ in range(N):
    word = input()
    trie.insert(word)

count = 0
for _ in range(M):
    S = input()
    if trie.is_prefix(S):
        count += 1

print(count)
