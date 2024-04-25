def change(n, k):
    tenary = ''
    while n != 0:
        remain = n % k
        tenary = str(remain) + tenary
        n //= k
    return tenary


tenary = 'qwe'
print(len(tenary))
