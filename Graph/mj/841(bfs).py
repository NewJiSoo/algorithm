# https://leetcode.com/problems/keys-and-rooms/description/

from collections import deque


def visitRooms(rooms):
    visited = [False] * len(rooms)

    # v에 연결되어있는 모든 vertex에 방문
    def bfs(v):
        q = deque()
        q.append(v)
        visited[v] = True
        while q:
            cur_v = q.popleft()
            for next_v in rooms[cur_v]:
                if not visited[next_v]:
                    q.append(next_v)
                    visited[next_v] = True

    bfs(0)
    return all(visited)


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(visitRooms(rooms))
