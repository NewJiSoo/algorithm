def change(n, k):
    tenary = ''
    while n != 0:
        remain = n % k
        tenary = str(remain) + tenary
        n //= k
    return tenary


# tenary = 'qwe'
# print(len(tenary))
 # 문자, 숫자 둘다 가능하지만           #꼭 하나여야 함
# print(chr(ord('A')))

dic = {chr(i): i - 64 for i in range(65, 91)}
arr = [chr(i) for i in range(ord('a'), ord('z'))]
dic2 = {chr(i): i - ord('a')+1 for i in range(ord('a'), ord('z'))}

print(dic)
print(arr)
print(dic2)
