arr = []
for idx, item in enumerate([2, 1, 3, 2]):
    arr.append((idx, item))

arr = sorted(arr, key=lambda x: x[1])

print(arr)
