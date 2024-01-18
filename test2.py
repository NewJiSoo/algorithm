from sys import stdin
n, m = map(int, stdin.readline().split())
stations = list(map(int, stdin.readline().split()))
preb_station = [0]*1000001
next_station = [0]*1000001

answer = [0]*m
count = 0

for k, std in enumerate(stations):
    pi = k-1
    ni = (k+1) % n
    preb_station[std] = stations[pi]
    next_station[std] = stations[ni]


def do_answer(i):
    global count
    answer[count] = i
    count += 1


def print_answer(answer):
    s = '\n'.join(map(str, answer))
    print(s)


def BN(i, j):
    nxt = next_station[i]
    do_answer(nxt)
    insert_j_after(i, j)


def BP(i, j):
    prv = preb_station[i]
    do_answer(prv)
    insert_j_after(prv, j)


def insert_j_after(i, j):
    nxt = next_station[i]
    next_station[i] = j
    next_station[j] = nxt
    preb_station[j] = i
    preb_station[nxt] = j


def CN(i):
    nxt = next_station[i]
    do_answer(nxt)
    remove(nxt)


def CP(i):
    prv = preb_station[i]
    do_answer(prv)
    remove(prv)


def remove(i):
    prv = preb_station[i]
    nxt = next_station[i]
    preb_station[nxt] = prv
    next_station[prv] = nxt


for _ in range(m):
    cmd = stdin.readline().split()
    if cmd[0] == 'BN':
        BN(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'BP':
        BP(int(cmd[1]), int(cmd[2]))
    elif cmd[0] == 'CN':
        CN(int(cmd[1]))
    elif cmd[0] == 'CP':
        CP(int(cmd[1]))

print_answer(answer)
