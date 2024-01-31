parents = [i for i in range(MAX_SIZE)]


def find(parent, x):
    if parent[x] == x:
        return x

    # 경로 압축(Path Compression)
    # find 하면서 만나는 모든 값의 부모 노드를 root로 만듦.
    parent[x] = find(parent, parent[x])
    return parent[x]


rank = [0 for _ in range(MAX_SIZE)]


# find()는 위와 동일
def union(parent, x, y, rank):
    rootX = find(parent, x)
    rootY = find(parent, y)

    # 두 값의 root가 같으면(이미 같은 트리) 연결 X(합치지 않음)
    if rootX == rootY:
        return

    # union-by-rank 최적화
    # 항상 높이가 더 낮은 트리를 높이가 높은 트리 밑에 넣음.
    # --> 높이가 더 높은 쪽을 root로 함.
    if rank[rootX] < rank[rootY]:
        parent[rootX] = rootY
    else:
        parent[rootY] = rootX
        if rank[rootX] == rank[rootY]:
            rank[rootX] += 1    # 만약 높이가 같다면 합친 후 -> x 높이 + 1
