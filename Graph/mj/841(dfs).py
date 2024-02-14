# https://leetcode.com/problems/keys-and-rooms/description/

def visitRooms(rooms):
    visited = [False] * len(rooms)

    # v에 연결되어있는 모든 vertex에 방문
    def dfs(v):
        visited[v] = True
        for i in rooms[v]:
            if not visited[i]:  # 시간복잡도 O(1)
                dfs(i)

    dfs(0)
    return all(visited)

    # if len(visited) == len(rooms):
    #     return True
    # else:
    #     return False


rooms = [[1, 3], [2, 4], [0], [4], [], [3, 4]]
print(visitRooms(rooms))
